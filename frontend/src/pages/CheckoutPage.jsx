import { useState } from "react";
import { loadStripe } from "@stripe/stripe-js";

const stripePromise = loadStripe("pk_test_51TOiPRIlqypzYkQOXY8dDEHPiprEjw5nzeEAoPGviLKpqIoKrtSApkxVTEGsUnCvwvex00Vq0YlrU6");

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

  const onChangeAddress1 = (e) => setInputAddress(prev => ({ ...prev, addressLine1: e.target.value }));
  const onChangeAddress2 = (e) => setInputAddress(prev => ({ ...prev, addressLine2: e.target.value }));
  const onChangeCity     = (e) => setInputAddress(prev => ({ ...prev, city: e.target.value }));
  const onChangeState    = (e) => setInputAddress(prev => ({ ...prev, state: e.target.value }));
  const onChangeZip      = (e) => setInputAddress(prev => ({ ...prev, zipCode: e.target.value }));
  const clearAddress     = () => setInputAddress(emptyAddress);

const handleCheckout = async () => {
    const cartItems = Array.from(cart.entries.values()).map(item => ({
        name: item.name,
        price: item.price,
        quantity: item.quantity
    }));

    const response = await fetch("/api/create-checkout-session/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ cart: cartItems })
    });

    const session = await response.json();
    const stripe = await stripePromise;

    await stripe.redirectToCheckout({ sessionId: session.sessionId });
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
            <td>➡️</td>
            <td><b>{cart.totalQty} item(s)</b></td>
            <td><b>${Math.trunc(cart.totalCost * 100) / 100}</b></td>
          </tr>
        </tbody>
      </table>

      <h2>Shipping Address</h2>

      <div>
        Street Address 1:
        <input type="text" value={inputAddress.addressLine1} onChange={onChangeAddress1} />
      </div>

      <div>
        Street Address 2:
        <input type="text" value={inputAddress.addressLine2} onChange={onChangeAddress2} />
      </div>

      <div>
        City:
        <input type="text" value={inputAddress.city} onChange={onChangeCity} />
      </div>

      <div>
        State:
        <select value={inputAddress.state} onChange={onChangeState}>
          {states.map(state => (
            <option key={state} value={state}>{state}</option>
          ))}
        </select>
      </div>

      <div>
        Zip Code:
        <input type="text" maxLength="5" value={inputAddress.zipCode} onChange={onChangeZip} />
      </div>

      <button onClick={clearAddress}>❌ Clear Address</button>
      <button onClick={handleCheckout}>💳 Pay Now</button>

    </div>
  );
}

export default CheckoutPage;