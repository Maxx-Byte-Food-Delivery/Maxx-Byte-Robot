import React, { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";

const OrderDetails = () => {
  const { id } = useParams(); // URL: /orders/:id
  const [order, setOrder] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/api/orders/${id}/`)
      .then((res) => {
        if (!res.ok) {
          throw new Error("Failed to fetch order");
        }
        return res.json();
      })
      .then((data) => {
        setOrder(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error(err);
        setError(err.message);
        setLoading(false);
      });
  }, [id]);

  if (loading) return <p>Loading order...</p>;
  if (error) return <p>Error: {error}</p>;
  if (!order) return <p>Order not found</p>;

  return (
    <div>
      <h1>
        <strong>Date:</strong>{" "}
        {new Date(order.created_at).toLocaleString()}
      </h1>

      <h2>Order Items:</h2>

      <ul>
        {order.order_items?.map((item) => (
          <li key={item.id}>
            {item.product.name} - Qty: {item.quantity} - $
            {item.product.price} × {item.quantity} = $
            {Number(item.subtotal).toFixed(2)}
          </li>
        ))}
      </ul>

      <p>
        <strong>Total:</strong> ${order.total_cost}
      </p>

      <p>
        <Link to="/history">Back to History</Link>
      </p>
    </div>
  );
};

export default OrderDetails;