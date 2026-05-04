function ClearCartButton({ clearCart, disabled }) {
    return (
        <button onClick={clearCart} disabled={disabled}>
            ❌🛒 Clear Cart
        </button>
    );
}

export default ClearCartButton;