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

   // ✅ PURE JS time ago function
  function timeAgo(dateString) {
    if (!dateString) return "Never updated";

    const now = new Date();
    const past = new Date(dateString);

    const seconds = Math.floor((now - past) / 1000);

    if (seconds < 60) return "Just now";

    const minutes = Math.floor(seconds / 60);
    if (minutes < 60) {
      return `${minutes} minute${minutes !== 1 ? "s" : ""} ago`;
    }

    const hours = Math.floor(minutes / 60);
    if (hours < 24) {
      return `${hours} hour${hours !== 1 ? "s" : ""} ago`;
    }

    const days = Math.floor(hours / 24);
    return `${days} day${days !== 1 ? "s" : ""} ago`;
  }

  return (
    <div style={{ padding: "20px", display: "flex", flexDirection: "column", alignItems: "center", backgroundColor: "#121212", minHeight: "100vh", color: "grey" }}>

      {/* EVERYTHING BELOW IS UNCHANGED UI */}
      <h1 style={{ marginBottom: "20px", fontSize: "42px", fontWeight: "bold" }}>
        View Order History
      </h1>
      
      <form onSubmit={handleSearch} style={{ marginBottom: "30px", display: "flex", gap: "10px" }}>
        <input 
          type="text" 
          placeholder="Search by item name" 
          value={item} 
          onChange={(e) => setItem(e.target.value)} 
          style={{ padding: "10px", borderRadius: "4px", border: "1px solid #444", backgroundColor: "#222", color: "white" }}
        />
        <input 
          type="date" 
          value={date} 
          onChange={(e) => setDate(e.target.value)} 
          style={{padding: "5px" }}
        />
        <button type="submit" style={{ padding: "10px 20px", cursor: "pointer", backgroundColor: "#504c4c", border: "none", fontWeight: "bold" }}>
          Search
          </button>
      </form>

      {orders.length === 0 ? (
        <p>No orders found matching your search parameters.</p>
      ) : (

        

        <ul style={{ listStyleType: "none", padding: 0 }}>
          {orders.map((order) => (
            <li key={order.id} style={{ border: "1px solid #ccc", padding: "30px", marginBottom: "10px", borderRadius: "6px" }}>
              <div style={{ display: "flex", justifyContent: "between", alignItems: "center", marginBottom: "10px" }}>
                <div>
                  <strong> Items:</strong>{" "}

                  {Array.isArray(order.order_items) && order.order_items.length > 0
                    ? order.order_items.map((item, index) => (
                        <span key={index}>
                          {item.product_name} x{item.quantity}
                          {index !== order.order_items.length - 1 ? ", " : ""}
                        </span>
                      ))
                    : "No items"} |
                  <strong> Order ID:</strong> #{order.id} | 
                  <strong> Address:</strong> {order.address|| " "} |
                  <strong> Status:</strong> {order.status} | 
                  <strong> Total:</strong> ${order.total_price} | 
                  <strong> Date:</strong> {new Date(order.created_at).toLocaleDateString()} |
                  <strong> Updated At:</strong>{" "}{order.updated_at ? new Date(order.updated_at).toLocaleString(): "N/A"}
                  
                </div>
                <strong> Action:</strong><button onClick={() => handleReorder(order.id)} style={{ marginLeft: "15px", cursor: "pointer" }}>
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