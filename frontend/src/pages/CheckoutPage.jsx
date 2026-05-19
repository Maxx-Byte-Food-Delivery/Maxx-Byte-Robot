import { useState } from "react";

const states = [
  "AL","AK","AR","AZ","CA","CO","CT","DE","FL","GA",
  "HI","IA","ID","IL","IN","KS","KY","LA","MA","MD",
  "ME","MI","MN","MO","MS","MT","NC","ND","NE","NH",
  "NJ","NM","NV","NY","OH","OK","OR","PA","RI","SC",
  "SD","TN","TX","UT","VA","VT","WA","WI","WV","WY"
];

const emptyAddress = {
  addressLine1: "",
  addressLine2: "",
  city: "",
  state: "AL",
  zipCode: ""
};

function CheckoutPage({ cart }) {

  const [inputAddress, setInputAddress] = useState(emptyAddress);

  const onChange = (field) => (e) =>
    setInputAddress(prev => ({ ...prev, [field]: e.target.value }));

  const clearAddress = () => setInputAddress(emptyAddress);

  const handleCheckout = async () => {
    // ✅ FIX 1: Read the token before making any requests
    const token = localStorage.getItem("access_token");
    if (!token) {
      console.error("User is not logged in.");
      // Optionally redirect: window.location.href = "/login";
      return;
    }

    // ✅ FIX 2: Reusable auth headers object
    const authHeaders = {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`,  // Use "Token" instead if using DRF TokenAuth
    };

    try {
      // Step 1: Create order from server-side cart
      const orderResponse = await fetch("http://localhost:8000/api/orders/create/", {
        method: "POST",
        headers: authHeaders,             // ✅ was missing Authorization
        body: JSON.stringify({ shipping_address: inputAddress })
      });

      // ✅ FIX 3: Check HTTP status before parsing JSON
      if (!orderResponse.ok) {
        const errData = await orderResponse.json();
        console.error("Order creation failed:", errData);
        return;
      }

      const orderData = await orderResponse.json();

      // Step 2: Create Stripe session
      const response = await fetch(
        `http://localhost:8000/api/payments/create-checkout-session/${orderData.order_id}/`,
        {
          method: "POST",
          headers: authHeaders,           // ✅ was missing Authorization
        }
      );

      if (!response.ok) {
        const errData = await response.json();
        console.error("Stripe session error:", errData);
        return;
      }

      const data = await response.json();
      window.location.href = data.url;

    } catch (err) {
      console.error("Checkout failed:", err);
    }
  };

  return (
    <div>
      <h1>Checkout</h1>
      <table>
        <tbody>
          {Array.from(cart.entries.values()).map((item, index) => (
            <tr key={index}>
              <td>{item.name}</td>
              <td>${item.price}</td>
              <td>{item.quantity}</td>
              <td>${item.price * item.quantity}</td>
            </tr>
          ))}
          <tr>
            <td><b>TOTAL</b></td>
            <td></td>
            <td><b>{cart.totalQty} items</b></td>
            <td><b>${cart.totalCost}</b></td>
          </tr>
        </tbody>
      </table>

      <h2>Shipping Address</h2>

      <input placeholder="Address 1"
        value={inputAddress.addressLine1}
        onChange={onChange("addressLine1")}
      />
      <input placeholder="Address 2"
        value={inputAddress.addressLine2}
        onChange={onChange("addressLine2")}
      />
      <input placeholder="City"
        value={inputAddress.city}
        onChange={onChange("city")}
      />
      <select value={inputAddress.state} onChange={onChange("state")}>
        {states.map(s => (
          <option key={s} value={s}>{s}</option>
        ))}
      </select>
      <input
        placeholder="Zip"
        maxLength="5"
        value={inputAddress.zipCode}
        onChange={onChange("zipCode")}
      />

      <button onClick={clearAddress}>❌ Clear Address</button>
      <button
        type="button"
        onClick={handleCheckout}
        disabled={cart.totalQty <= 0}
      >
        💳 CHECKOUT
      </button>
    </div>
  );
}

export default CheckoutPage;