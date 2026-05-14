import React, { useEffect, useState } from "react";

function OrderHistory() {

  const [orders, setOrders] = useState([]);
  const [item, setItem] = useState("");
  const [date, setDate] = useState("");

  const userId = localStorage.getItem("user_id");
  const accessToken = localStorage.getItem("access_token");

  // Fetch orders from backend
  const fetchOrders = async () => {

    try {

      let url = `http://127.0.0.1:8000/api/users/${userId}/orders/view_history/`;

      // Search params
      const params = new URLSearchParams();

      if (item) {
        params.append("item", item);
      }

      if (date) {
        params.append("date", date);
      }

      // Add query params to URL
      if ([...params].length > 0) {
        url += `?${params.toString()}`;
      }

      // API request
      const res = await fetch(url, {
        method: "GET",

        headers: {
          "Authorization": `Bearer ${accessToken}`,
          "Content-Type": "application/json",
        },
      });

      const data = await res.json();

      console.log("Orders:", data);

      // Prevent map() crash
      setOrders(Array.isArray(data) ? data : []);

    } catch (error) {

      console.error("Error fetching orders:", error);

      setOrders([]);
    }
  };

  // Load orders on page start
  useEffect(() => {
    fetchOrders();
  }, []);

  // Search submit
  const handleSearch = (e) => {
    e.preventDefault();
    fetchOrders();
  };

  // Reorder
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

          body: JSON.stringify({
            order_id: orderId,
          }),
        }
      );

      const data = await res.json();

      alert(data.message);

      // Refresh orders after reorder
      fetchOrders();

    } catch (error) {

      console.error("Reorder error:", error);

      alert("Failed to reorder.");
    }
  };

  return (

    <div
      style={{
        padding: "20px",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
      }}
    >

      {/* Title */}
      <h1 style={{marginBottom: "20px", fontSize: "42px", fontWeight: "bold",}}>View Order History</h1>

      {/* Search Form */}
      <form
        onSubmit={handleSearch}
        style={{
          marginBottom: "20px",
          display: "flex",
          gap: "10px",
          alignItems: "center",
          justifyContent: "center",
        }}
      >

        {/* Search by item */}
        <input
          type="text"
          placeholder="Search by item name"
          value={item}
          onChange={(e) => setItem(e.target.value)}
          style={{
            padding: "8px",
          }}
        />

        {/* Date filter */}
        <input
          type="date"
          value={date}
          onChange={(e) => setDate(e.target.value)}
          style={{
            padding: "8px",
          }}
        />

        {/* Search button */}
        <button
          type="submit"
          style={{
            padding: "8px 15px",
            cursor: "pointer",
          }}
        >
          Search
        </button>

      </form>

      {/* Orders Table */}
      <table
        border="1"
        cellPadding="10"
        cellSpacing="0"
        width="90%"
        style={{
          textAlign: "center",
          borderCollapse: "collapse",
        }}
      >

        <thead
          style={{
            backgroundColor: "#f2f2f2",
          }}
        >

          <tr>

            <th>Order ID</th>

            <th>Address</th>

            <th>Total Price</th>

            <th>Status</th>

            <th>Created At</th>

            <th>Items</th>

            <th>Action</th>

          </tr>

        </thead>

        <tbody>

          {orders.length > 0 ? (

            orders.map((order) => (

              <tr key={order.id}>

                {/* Order ID */}
                <td>
                  #{order.id}
                </td>

                {/* Address */}
                <td>
                  {order.address}
                </td>

                {/* Total Price */}
                <td>
                  ${order.total_price}
                </td>

                {/* Status */}
                <td>
                  {order.status}
                </td>

                {/* Created Date */}
                <td>
                  {new Date(order.created_at).toLocaleString()}
                </td>

                {/* Order Items */}
                <td>

                  {order.order_items &&
                  order.order_items.length > 0 ? (

                    order.order_items.map((item) => (

                      <div key={item.id}>

                        • {item.product?.name} x {item.quantity}

                      </div>
                    ))

                  ) : (

                    <div>No items</div>
                  )}

                </td>

                {/* Reorder Button */}
                <td>

                  <button
                    onClick={() => handleReorder(order.id)}
                    style={{
                      padding: "5px 10px",
                      cursor: "pointer",
                    }}
                  >
                    Reorder
                  </button>

                </td>

              </tr>
            ))

          ) : (

            <tr>

              <td
                colSpan="7"
                align="center"
                style={{
                  padding: "20px",
                }}
              >

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