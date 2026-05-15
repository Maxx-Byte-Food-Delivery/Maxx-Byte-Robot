import React, { useEffect, useState } from "react";
import API from "../api/api";

function OrderHistory() {
  const [orders, setOrders] = useState([]);
  const [item, setItem] = useState('');
  const [date, setDate] = useState('');

  // Fetch orders securely using your custom interceptor wrapper instance
  const fetchOrders = async () => {
    try {
      const response = await API.get('/orders/view_history/', {
        params: {
          item: item || undefined, // Drops parameter from string query if empty
          date: date || undefined
        }
      });

      const data = response.data;

      if (Array.isArray(data)) {
        setOrders(data);
      } else {
        console.error("API did not return a clean data list array:", data);
        setOrders([]);
      }
    } catch (error) {
      console.error("Failed to load user order records:", error);
      setOrders([]);
    }
  };

  // Automatically fetch records when the application page loads
  useEffect(() => {
    fetchOrders();
  }, []);

  const handleSearch = (e) => {
    e.preventDefault();
    fetchOrders();
  };

  const handleReorder = async (orderId) => {
    try {
      const response = await API.post(`/orders/reorder/${orderId}/`, {
        order_id: orderId
      });
      alert(response.data.message || "Order re-submitted successfully!");
    } catch (error) {
      console.error("Reorder request action failed:", error);
      alert("Could not process your reorder request.");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>View Order History</h1>
      
      <form onSubmit={handleSearch} style={{ marginBottom: "20px" }}>
        <input 
          type="text" 
          placeholder="Search by item name" 
          value={item} 
          onChange={(e) => setItem(e.target.value)} 
          style={{ marginRight: "10px", padding: "5px" }}
        />
        <input 
          type="date" 
          value={date} 
          onChange={(e) => setDate(e.target.value)} 
          style={{ marginRight: "10px", padding: "5px" }}
        />
        <button type="submit" style={{ padding: "5px 15px" }}>Search</button>
      </form>

      {orders.length === 0 ? (
        <p>No orders found matching your search parameters.</p>
      ) : (
        <ul style={{ listStyleType: "none", padding: 0 }}>
          {orders.map((order) => (
            <li key={order.id} style={{ border: "1px solid #ccc", padding: "15px", marginBottom: "10px", borderRadius: "6px" }}>
              <div style={{ display: "flex", justifyContent: "between", alignItems: "center", marginBottom: "10px" }}>
                <div>
                  <strong>Order ID:</strong> #{order.id} | 
                  <strong> Status:</strong> {order.status} | 
                  <strong> Total:</strong> ${order.total_price} | 
                  <strong> Date:</strong> {new Date(order.created_at).toLocaleDateString()}
                </div>
                <button onClick={() => handleReorder(order.id)} style={{ marginLeft: "15px", cursor: "pointer" }}>
                  Reorder Item Layout
                </button>
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default OrderHistory;
