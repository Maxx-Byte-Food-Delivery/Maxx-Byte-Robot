import React, { useEffect, useState } from "react";

function OrderHistory() {
  const [orders, setOrders] = useState([]);
  const [item, setItem] = useState("");
  const [date, setDate] = useState("");

  // Fetch orders
  const fetchOrders = async () => {
    let url = "http://127.0.0.1:8000/api/orders/";

    const params = new URLSearchParams();
    if (item) params.append("item", item);
    if (date) params.append("date", date);

    if ([...params].length > 0) {
      url += `?${params.toString()}`;
    }

    const res = await fetch(url);
    const data = await res.json();
    setOrders(data);
  };

  useEffect(() => {
    fetchOrders(); // load on page start
  }, []);

  const handleSearch = (e) => {
    e.preventDefault();
    fetchOrders();
  };

  const handleReorder = async (orderId) => {
    const res = await fetch("http://127.0.0.1:8000/api/reorder/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ order_id: orderId }),
    });

    const data = await res.json();
    alert(data.message);
  };

  return (
    <div>
      <h1>View Order History</h1>

      <form onSubmit={handleSearch}>
        <input
          type="text"
          placeholder="Search by item name"
          value={item}
          onChange={(e) => setItem(e.target.value)}
        />

        <input
          type="date"
          value={date}
          onChange={(e) => setDate(e.target.value)}
        />

        <button type="submit">Search</button>
      </form>

      <ul>
        {orders.map((order) => (
          <li key={order.id}>
            <div>
              <strong>Date:</strong>{" "}
              {new Date(order.created_at).toLocaleString()}
            </div>

            <button onClick={() => handleReorder(order.id)}>
              Reorder
            </button>

            <div>
              {order.order_items.map((item) => (
                <div key={item.id}>• {item.product.name}</div>
              ))}
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default OrderHistory;