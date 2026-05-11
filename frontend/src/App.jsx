import React, { useEffect, useState } from "react";
<<<<<<< HEAD
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import Login from "./Login";
import Page from "./Page";
import OrderHistory from "./history";
import ActiveOrders from "./ActiveOrders";
=======
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
>>>>>>> 7d36b6ecddca7a73625fc4d68d6422069df92bb8

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

      </Routes>
    </BrowserRouter>
  );
}

export default App;