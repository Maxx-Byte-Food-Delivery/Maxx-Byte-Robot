import ClearCartButton from "../components/ClearCartButton";
import { CartEntry } from "../models/CartEntry";

function CartPage({ cart, clearCart, setCart }) {
  const entries = Array.from(cart.entries.values());

  function removeItemEntirely(product) {
    setCart(prevCart => {
      const updated = new Map(prevCart.entries);
      const removeQty = updated.get(product.name).quantity;
      const removePrice = updated.get(product.name).price * removeQty;
      updated.delete(product.name);
      return {
        entries: updated,
        totalQty: prevCart.totalQty - removeQty,
        totalCost: prevCart.totalCost - removePrice
      };
    });
    showToast(`${product.name} was removed entirely from cart.`, false);
  }

  function addOneMore(product){
    setCart(prevCart => {
      const updated = new Map(prevCart.entries);
      const qty = updated.get(product.name).quantity;
      updated.set(product.name, new CartEntry(product.name, product.price, qty + 1));
      return {
        entries: updated,
        totalQty: prevCart.totalQty + 1,
        totalCost: prevCart.totalCost + product.price
      };
    });
  }

  function removeOne(product){
    setCart(prevCart => {
      const updated = new Map(prevCart.entries);
      const toDecrease = updated.get(product.name).quantity;
      let removeQty = 0;
      let removePrice = 0;
      if(toDecrease > 1){
        removeQty = 1;
        removePrice = updated.get(product.name).price;
        updated.set(product.name, new CartEntry(product.name, product.price, toDecrease - 1));
      }
      else{
        removeQty = updated.get(product.name).quantity;
        removePrice = updated.get(product.name).price * removeQty;
        updated.delete(product.name);
      }
      return {
        entries: updated,
        totalQty: prevCart.totalQty - removeQty,
        totalCost: prevCart.totalCost - removePrice
      };
    });
  }

  return (
    <div>
      <h1>Cart</h1>
      {entries.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        entries.map((entry) => (
          <div key={entry.name}>
            <p>{entry.name} x {entry.quantity} — ${entry.price * entry.quantity}</p>
            <button onClick={() => removeItemEntirely(entry)}>🚫</button>
            <button onClick={() => removeOne(entry)}>➖</button>
            <button onClick={() => addOneMore(entry)}>➕</button>
          </div>
        ))
      )}
      <h3>Total: ${Math.trunc(cart.totalCost * 100) / 100}</h3>
      <ClearCartButton clearCart={clearCart} disabled={entries.length === 0} />
    </div>
  );
}

export default CartPage;