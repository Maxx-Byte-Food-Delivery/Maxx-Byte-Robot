import React, { useEffect, useState } from "react";
import "./App.css";

import MFAOptions from "./MFAOptions";
import VerifySMS from "./VerifySMS";
import VerifyTOTP from "./VerifyTOTP";
import SetupTOTP from "./SetupTOTP";
import ConfirmTOTP from "./ConfirmTOTP";
import Settings from "./Settings";
import Staff from "./Staff";
import Student from "./Student";
import Login from "./pages/Login";
import Page from "./pages/Page";
import OrderHistory from "./history";
import CartPage from "./pages/CartPage";
import CheckoutPage from "./pages/CheckoutPage";
import Products from "./pages/Products";
import NavigationBar from "./components/NavigationBar";

import { BrowserRouter, Routes, Route } from "react-router-dom";

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

      {/* Navbar appears on all pages */}
      <NavigationBar cart={cart} />

      <Routes>

        {/* Home / Login */}
        <Route path="/" element={<Login />} />

        {/* Products */}
        <Route
          path="/products"
          element={<Products cart={cart} setCart={setCart} />}
        />

        {/* Cart */}
        <Route
          path="/cart"
          element={<CartPage cart={cart} clearCart={clearCart} />}
        />

        {/* Checkout */}
        <Route
          path="/checkout"
          element={<CheckoutPage cart={cart} />}
        />

        {/* Orders */}
        <Route
          path="/orders"
          element={<OrderHistory />}
        />

        {/* Pages */}
        <Route path="/page" element={<Page />} />

        {/* MFA */}
        <Route path="/mfa-options" element={<MFAOptions />} />
        <Route path="/verify-sms" element={<VerifySMS />} />
        <Route path="/verify-totp" element={<VerifyTOTP />} />
        <Route path="/setup-totp" element={<SetupTOTP />} />
        <Route path="/confirm-totp" element={<ConfirmTOTP />} />

        {/* Dashboards */}
        <Route path="/staff" element={<Staff />} />
        <Route path="/student" element={<Student />} />

        {/* Settings */}
        <Route path="/settings" element={<Settings />} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;