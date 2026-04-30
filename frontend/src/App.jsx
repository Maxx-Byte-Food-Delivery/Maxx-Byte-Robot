import React, { useEffect, useState } from "react";
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import Login from "./Login";
import Page from "./Page";
import VerifyMFA from "./VerifyMFA";
import Staff from "./Staff";
import Student from "./Student";
import Settings from "./Settings";

import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";


function App() {
  const [count, setCount] = useState(0)
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/hello")
      .then(res => res.json())
      .then(data => {
        setMessage(data.message);
        console.log(data);
      })
      .catch(err => console.error(err));
  }, []);
  
  return(
    <BrowserRouter>

      <Routes>

        {/* Login page */}
        <Route
          path="/"
          element={<Login />}
        />

        {/* MFA Verification */}
        <Route
          path="/verify-mfa"
          element={<VerifyMFA />}
        />

        {/* Staff Dashboard */}
        <Route
          path="/staff"
          element={<Staff />}
        />

        {/* Student Dashboard */}
        <Route
          path="/student"
          element={<Student />}
        />

        <Route
          path="/settings"
          element={<Settings />}
        />


        {/* Classes page */}
        <Route
          path="/page"
          element={<Page />}
        /> 

      </Routes>

    </BrowserRouter>
  )

  
}
export default App;
