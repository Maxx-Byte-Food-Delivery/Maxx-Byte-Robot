import { loadStripe } from "@stripe/stripe-js";

const stripePromise = loadStripe("pk_test_51TOiPRIlqypzYkQOXY8dDEHPiprEjw5nzeEAoPGviLKpqIoKrtSApkxVTEMb6F85L6YW7fbV2RtVFEGsUnCvwvex00Vq0YlrU6");

function CheckoutPage() {
    const handleCheckout = async () => {
        const response = await fetch("http://localhost:8000/api/create-checkout-session/", {
            method: "POST"
        });

        const session = await response.json();

        const stripe = await stripePromise;

        await stripe.redirectToCheckout({
            sessionId: session.sessionId
        });
    };

    return (
        <div>
            <h1>Checkout</h1>
            <button onClick={handleCheckout}>
                Pay Now
            </button>
        </div>
    );
}

export default CheckoutPage;