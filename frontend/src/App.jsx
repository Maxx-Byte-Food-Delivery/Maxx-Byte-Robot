import React, { useEffect, useState } from "react";
import './App.css';

import Login from "./Login";
import Page from "./Page";
import Staff from "./Staff";
import Student from "./Student";
import Settings from "./Settings";

import VerifySMS from "./VerifySMS";
import VerifyTOTP from "./VerifyTOTP";
import SetupTOTP from "./SetupTOTP";
import ConfirmTOTP from "./ConfirmTOTP";
import MFAOptions from "./MFAOptions"

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