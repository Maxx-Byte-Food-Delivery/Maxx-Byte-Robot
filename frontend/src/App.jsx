import React, { useEffect, useState } from "react";
import "./App.css";

import MFAOptions from "./pages/MFAOptions";
import VerifySMS from "./pages/VerifySMS";
import VerifyTOTP from "./pages/VerifyTOTP";
import SetupTOTP from "./pages/SetupTOTP";
import ConfirmTOTP from "./pages/ConfirmTOTP";
import Settings from "./pages/Settings";
import Staff from "./pages/Staff";
import Student from "./pages/Student";
import Login from "./pages/Login";
import CartPage from "./pages/CartPage";
import CheckoutPage from "./pages/CheckoutPage";
import Products from "./pages/Products";
import NavigationBar from "./components/NavigationBar";
import OrderHistory from "./pages/history";
import SetupSMS from "./pages/SetupSMS";
import ActiveOrders from "./pages/ActiveOrders";

import { BrowserRouter, Routes, Route } from "react-router-dom";

import { useLocation } from "react-router-dom";

function AppContent({ cart, setCart, clearCart }) {
  const location = useLocation();

  // Hide navbar only on login page
  const hideNavbar = location.pathname === "/";

  return (
    <>
      {!hideNavbar && <NavigationBar cart={cart} />}

      <Routes>

        <Route path="/" element={<Login />} />

        <Route path="/tracker" element={<ActiveOrders/>} />

        <Route
          path="/products"
          element={<Products cart={cart} setCart={setCart} />}
        />

        <Route
          path="/cart"
          element={<CartPage cart={cart} clearCart={clearCart} />}
        />

        <Route
          path="/checkout"
          element={<CheckoutPage cart={cart} />}
        />

        <Route path="/orders" element={<OrderHistory />} />

        <Route path="/mfa-options" element={<MFAOptions />} />
        <Route path="/verify-sms" element={<VerifySMS />} />
        <Route path="/verify-totp" element={<VerifyTOTP />} />
        <Route path="/setup-totp" element={<SetupTOTP />} />
        <Route path="/confirm-totp" element={<ConfirmTOTP />} />

        <Route path="/setup-sms" element={<SetupSMS />} />

        <Route path="/staff" element={<Staff />} />
        <Route path="/student" element={<Student />} />

        <Route path="/settings" element={<Settings />} />

      </Routes>
    </>
  );
}

function App() {
  const [message, setMessage] = useState("");

  const [cart, setCart] = useState({
    entries: new Map(),
    totalQty: 0,
    totalCost: 0
  });

  // CSRF init
  useEffect(() => {
    const initCSRF = async () => {
      try {
        await fetch("http://localhost:8000/api/csrf/", {
          credentials: "include",
        });
      } catch (err) {
        console.error("CSRF init failed", err);
      }
    };

    initCSRF();
  }, []);

  // ✅ clear cart function
  const clearCart = () => {
    setCart({
      entries: new Map(),
      totalQty: 0,
      totalCost: 0
    });
  };

  return (
    <BrowserRouter>
      <AppContent
        cart={cart}
        setCart={setCart}
        clearCart={clearCart}
      />
    </BrowserRouter>
  );
}

export default App;