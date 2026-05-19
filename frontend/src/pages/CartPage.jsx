import ClearCartButton from "../components/ClearCartButton";
import { CartEntry } from "../models/CartEntry";
import { Message } from "../models/Message";
import {useState, useEffect} from 'react';
import { showToast } from "../utils/toast";

function CartPage({ cart, clearCart, setCart, setMsg}) {
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
      //Set up the toast announcing that you've added one more of an item in the cart.
      setMsg(msg => new Message(`One more ${product.name} added to the cart, you now have ${qty + 1}.`, true));
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
        //Set up the toast announcing that you've removed one of an item in the cart.
        setMsg(msg => new Message(`One ${product.name} removed from the cart, you now have ${toDecrease - 1}.`, false));
        updated.set(product.name, new CartEntry(product.name, product.price, toDecrease - 1));
      }
      else{
        removeQty = updated.get(product.name).quantity;
        removePrice = updated.get(product.name).price * removeQty;
        //Set up the toast announcing that you've removed an item completely from the cart when qty is reduced to 0.
        setMsg(msg => new Message(`${product.name} was removed entirely from cart.`, false));
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
            {/*Use toFixed(2) to ensure proper display of money amounts.*/}
            <p>{entry.name} x {entry.quantity} — ${(entry.price * entry.quantity).toFixed(2)}</p>
            <button onClick={() => removeItemEntirely(entry)}>🚫</button>
            <button onClick={() => removeOne(entry)}>➖</button>
            <button onClick={() => addOneMore(entry)}>➕</button>
          </div>
        ))
      )}
      <h3>Total: ${cart.totalCost.toFixed(2)}</h3>
      <ClearCartButton clearCart={clearCart} disabled={entries.length === 0} />
    </div>
  );
}

export default CartPage;