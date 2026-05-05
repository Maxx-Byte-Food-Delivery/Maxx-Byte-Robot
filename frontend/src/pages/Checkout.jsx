import { loadStripe } from "@stripe/stripe-js";

const stripePromise = loadStripe("pk_test_51TOiPRIlqypzYkQOXY8dDEHPiprEjw5nzeEAoPGviLKpqIoKrtSApkxVTEMb6F85L6YW7fbV2RtVFEGsUnCvwvex00Vq0YlrU6");

function CheckoutPage() {

    const handleCheckout = async () => {

        const response = await fetch(
            "http://localhost:8000/api/create-checkout-session/",
            { method: "POST" }
        );

        const session = await response.json();

        const stripe = await stripePromise;

        await stripe.redirectToCheckout({
            sessionId: session.sessionId
        });
    };

    return (
        <div>

            <h1>Checkout</h1>

            <table>
                <tbody>
                    {
                        Array.from(currentCart.entries.values()).map((item, index) => (
                            <tr key={index}>
                                <td>{item.name}</td>
                                <td>${item.price}</td>
                                <td>{item.quantity}</td>
                                <td>${item.price * item.quantity}</td>
                            </tr>
                        ))
                    }

                    <tr>
                        <td><b>TOTAL</b></td>
                        <td>➡️</td>
                        <td><b>{currentCart.totalQty} item(s)</b></td>
                        <td><b>${Math.trunc(currentCart.totalCost * 100) / 100}</b></td>
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

            <button onClick={handleCheckout}>
                💳 Pay Now
            </button>

        </div>
    );
}

export default CheckoutPage;