// src/pages/customer/OrderPage.jsx
import { useState } from "react";
import { useSelector } from "react-redux";
import OrderForm from "../../components/ordering/OrderForm";
import OrderTracker from "../../components/ordering/OrderTracker";

export default function OrderPage() {
  const [view, setView] = useState("order"); // "order" | "track"
  const activeOrder = useSelector((s) => s.orders.activeOrder);

  return (
    <div className="order-page">
      <nav className="tab-bar">
        <button className={view === "order" ? "active" : ""} onClick={() => setView("order")}>
          New Order
        </button>
        <button className={view === "track" ? "active" : ""} onClick={() => setView("track")}>
          Track Order {activeOrder && `#${activeOrder.id}`}
        </button>
      </nav>

      {view === "order" && (
        <OrderForm onSuccess={() => setView("track")} />
      )}

      {view === "track" && (
        activeOrder
          ? <OrderTracker orderId={activeOrder.id} />
          : <p className="empty-state">No active order. Place an order first.</p>
      )}
    </div>
  );
}
