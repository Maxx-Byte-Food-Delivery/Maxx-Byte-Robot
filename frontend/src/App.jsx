import React, { useEffect, useState } from "react";
import './App.css';

import Login from "./Login";
import Page from "./Page";
import OrderHistory from "./history";
import CartPage from "./pages/CartPage";
import CheckoutPage from "./pages/CheckoutPage";
import Products from "./pages/Products";
import CartComponent from "./components/CartComponent";

import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

function App() {
  const [message, setMessage] = useState("");

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

  return (
    <BrowserRouter>
      <CartComponent/>
      <Routes>
        
        {/* Login page */}
        <Route
          path="/"
          element={<Login />}
        />

        {/* Classes page */}
        <Route
          path="/page"
          element={<Page />}
        />
        
        <Route
          path="/products"
          element={<Products />}
        />
        <Route
          path="/cart"
          element={<CartPage />}
        />
        {/*Checkout page*/}
        <Route 
        path="/checkout" 
        element={<CheckoutPage />} />

        <Route path="/orders" element={<OrderHistory />} />

        {/* Login */}
        <Route path="/" element={<Login />} />

        {/* 2FA Options*/}
        <Route path="/mfa-options" element={<MFAOptions />} />

        {/* 2FA */}
        <Route path="/verify-sms" element={<VerifySMS />} />
        <Route path="/verify-totp" element={<VerifyTOTP />} />

        {/* TOTP Setup */}
        <Route path="/setup-totp" element={<SetupTOTP />} />
        <Route path="/confirm-totp" element={<ConfirmTOTP />} />

        {/* Dashboards */}
        <Route path="/staff" element={<Staff />} />
        <Route path="/student" element={<Student />} />

        {/* Settings */}
        <Route path="/settings" element={<Settings />} />

        {/* Other */}
        <Route path="/page" element={<Page />} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;