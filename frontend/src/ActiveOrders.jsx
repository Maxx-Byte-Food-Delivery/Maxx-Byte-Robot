import {useState } from "react";

function ActiveOrders() {
  const updateQuantity = (index, qty) => {
    const newItems = [...items];
    newItems[index].qty = qty;
    setItems(newItems);
  };

  const saveChanges = () => {
    fetch(`http://localhost:8000/api/orders/${order.id}/`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        ...order,
        items: items
      })
    });
  };

  return (
    <div>
      <h4>Items</h4>

      {items.map((item, i) => (
        <div key={i}>
          <span>{item.name}</span>
          <input
            type="number"
            value={item.qty}
            onChange={(e) => updateQuantity(i, e.target.value)}
          />
        </div>
      ))}

      <button onClick={saveChanges}>Save Changes</button>
    </div>
  );
}