import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

function OrderHistory() {

  const [orders, setOrders] = useState([]);
  const [activeOrders, setActiveOrders] = useState([]); // ✅ ADDED ONLY
  const [item, setItem] = useState("");
  const [date, setDate] = useState("");

  const userId = localStorage.getItem("user_id");
  const accessToken = localStorage.getItem("access_token");

  // Fetch order history
  const fetchOrders = async () => {
    try {
      let url = `http://127.0.0.1:8000/api/users/${userId}/orders/view_history/`;

      const params = new URLSearchParams();

      if (item) params.append("item", item);
      if (date) params.append("date", date);

      if ([...params].length > 0) {
        url += `?${params.toString()}`;
      }

      const res = await fetch(url, {
        method: "GET",
        headers: {
          "Authorization": `Bearer ${accessToken}`,
          "Content-Type": "application/json",
        },
      });

      const data = await res.json();

      setOrders(Array.isArray(data) ? data : []);

    } catch (error) {
      console.error("Error fetching orders:", error);
      setOrders([]);
    }
  };

  // ✅ NEW: Fetch active orders (NO UI CHANGE)
  const fetchActiveOrders = async () => {
    try {
      const url = `http://127.0.0.1:8000/api/users/${userId}/orders/active_orders/`;

      const res = await fetch(url, {
        method: "GET",
        headers: {
          "Authorization": `Bearer ${accessToken}`,
          "Content-Type": "application/json",
        },
      });

      const data = await res.json();

      setActiveOrders(Array.isArray(data) ? data : []);

      console.log("Active Orders:", data); // optional debug only

    } catch (error) {
      console.error("Error fetching active orders:", error);
      setActiveOrders([]);
    }
  };

  class Order {
        id = "";
        address = "";
        totalPrice = 0;
        status = "";
        createdAt = "";
        orderItems = "";
        updatedAt = "";

      constructor(id, address, totalPrice, status, createdAt, orderItems, updatedAt) {
          this.id = id;
          this.address = address;
          this.totalPrice = totalPrice;
          this.status = status;
          this.createdAt = createdAt;
          this.orderItems = orderItems;
          this.updatedAt = updatedAt;
    
      }
  }


  const getStatusColor = (status) => {
      switch (status) {
        case "pending":
          return "#facc15"; // yellow
        case "confirmed":
          return "#60a5fa"; // blue
        case "preparing":
          return "#fb923c"; // orange
        case "ready":
          return "#a78bfa"; // purple
        case "dispatched":
          return "#38bdf8"; // sky
        case "delivered":
          return "#4ade80"; // green
        case "completed":
          return "#22c55e"; // green strong
        case "cancelled":
          return "#ef4444"; // red
        default:
          return "#d1d5db";
        }
      };

 
  

  // Load on page start
  useEffect(() => {
    fetchOrders();
    fetchActiveOrders(); // ✅ ADDED ONLY
  }, []);

  const handleSearch = (e) => {
    e.preventDefault();
    fetchOrders();
  };

  const handleReorder = async (orderId) => {
    try {
      const res = await fetch(
        `http://127.0.0.1:8000/api/users/${userId}/orders/reorder/${orderId}/`,
        {
          method: "POST",
          headers: {
            "Authorization": `Bearer ${accessToken}`,
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ order_id: orderId }),
        }
      );

      const data = await res.json();

      alert(data.message);

      fetchOrders();
      fetchActiveOrders(); // optional refresh

    } catch (error) {
      console.error("Reorder error:", error);
      alert("Failed to reorder.");
    }
  };

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
          style={{ padding: "8px" }}
        />

        <button type="submit" style={{ padding: "10px 20px", cursor: "pointer", backgroundColor: "#504c4c", border: "none", fontWeight: "bold" }}>
          Search
        </button>
      </form>

      <table border="0" cellPadding="15" style={{ width: "90%", borderCollapse: "collapse", backgroundColor: "#1e1e1e", borderRadius: "8px", overflow: "hidden" }}>
        <thead style={{ backgroundColor: "#f2f2f2" }}>
          <tr>
            <th>Order ID</th>
            <th>Address</th>
            <th>Total Price</th>
            <th>Status</th>
            <th>Created At</th>
            <th>Updated At</th>
            <th>Items</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>
          {orders.length > 0 ? (
            orders.map((order) => (
              <tr key={order.id} style={{ borderBottom: "1px solid #333" }}>
                <td>#{order.id}</td>
                <td>{order.address}</td>
                <td style={{ fontWeight: "bold" }}>${order.total_price}</td>
                <td>
                  <span style={{ color: getStatusColor(order.status), fontWeight: "bold", textTransform: "capitalize" }}>
                    {order.status}
                  </span>
                </td>
                <td>{new Date(order.created_at).toLocaleDateString()}</td>
                <td>{order.updated_at ? new Date(order.updated_at).toLocaleDateString() : "N/A"}</td>
                <td style={{ textAlign: "left" }}>
                  {order.order_items?.map((i) => (
                    <div key={i.id} style={{ fontSize: "14px" }}>• {i.product?.name} x {i.quantity}</div>
                  ))}
                </td>
                <td>
                  <button
                    onClick={() => handleReorder(order.id)}
                    style={{ padding: "6px 12px", cursor: "pointer", backgroundColor: "#444", color: "white", border: "1px solid #666", borderRadius: "4px" }}
                  >
                    Reorder
                  </button>
                </td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="8" style={{ padding: "40px", color: "#777" }}>
                No orders found
              </td>
            </tr>
          )}
        </tbody>
      </table>

    </div>
  );
}

export default OrderHistory;