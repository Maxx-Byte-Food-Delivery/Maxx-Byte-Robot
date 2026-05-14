import React, { useEffect, useState } from "react";
import './App.css';
import MFAOptions from "./pages/MFAOptions";
import VerifySMS from "./pages/VerifySMS";
import VerifyTOTP from "./pages/VerifyTOTP";
import SetupTOTP from "./pages/SetupTOTP";
import ConfirmTOTP from "./pages/ConfirmTOTP";
import Student from "./pages/Student";
import Staff from "./pages/Staff";
import Settings from "./pages/Settings";
import Login from "./pages/Login";
import Page from "./pages/Page";
import OrderHistory from "./components/history";
import OrderTracker from "./OrderTracker";

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
      <Routes>

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

        {/* Classes page */}
        <Route
          path="/page"
          element={<Page />}
        />
        <Route path="/orders" element={<OrderHistory />} />
        <Route path="/tracker" element={<OrderTracker />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;