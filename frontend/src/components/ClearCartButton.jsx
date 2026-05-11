function ClearCartButton({ clearCart, disabled }) {
  return (
    <button
      onClick={() => {
        console.log("Button clicked");
        clearCart();
      }}
      disabled={disabled}
    >
      Clear Cart
    </button>
  );
}

export default ClearCartButton;

