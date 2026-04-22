import React, { useEffect, useState } from "react";
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import Login from "./Login";
import Hello from "./Hello";
import {BrowserRouter, Routes,Route} from "react-router-dom";

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

  return (

    <BrowserRouter>

      <Routes>

        <Route
          path="/"
          element={<Login />}
        />

        <Route
          path="/hello"
          element={<Hello />}
        />

      </Routes>

    </BrowserRouter>

  );
}

export default App
