import ClearCartButton from "../components/ClearCartButton";

function CartPage({ cart, clearCart }) {
  const entries = Array.from(cart.entries.values());

  return (
    <div>
      <h1>Cart</h1>
      {entries.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        entries.map((entry) => (
          <div key={entry.name}>
            <p>{entry.name} x{entry.quantity} — ${entry.price * entry.quantity}</p>
          </div>
        ))
      )}
      <h3>Total: ${cart.totalCost}</h3>
      <ClearCartButton clearCart={clearCart} disabled={entries.length === 0} />
    </div>
  );
}

export default CartPage;