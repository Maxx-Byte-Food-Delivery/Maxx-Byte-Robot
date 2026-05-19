import { useState } from "react";

const states = [
  "AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA",
  "HI","ID","IL","IN","IA","KS","KY","LA","ME","MD",
  "MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ",
  "NM","NY","NC","ND","OH","OK","OR","PA","RI","SC",
  "SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"
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
    try {
      const cartItems = Array.from(cart.entries.values()).map(item => ({
        name: item.name,
        price: item.price,
        quantity: item.quantity
      }));

      const response = await fetch("http://localhost:8000/api/payments/create-checkout-session/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ cart: cartItems })
      });

      const data = await response.json();

      // ✅ Proper error handling
      if (!data.url) {
        console.error("Stripe session error:", data);
        return;
      }

      // ✅ Correct modern Stripe flow
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
              {/*Use toFixed(2) to ensure proper display of money amounts.*/}
              <td>${(item.price * item.quantity).toFixed(2)}</td>
            </tr>
          ))}

          <tr>
            <td><b>TOTAL</b></td>
            <td>➡️</td>
            <td><b>{cart.totalQty} items</b></td>
            <td><b>${(cart.totalCost.toFixed(2))}</b></td>
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

      <select
        value={inputAddress.state}
        onChange={onChange("state")}
      >
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

      <button onClick={clearAddress}>
        ❌ Clear Address
      </button>

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