import React, { useEffect, useState } from "react";
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

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
    <>
      <div>
        <h1> {message} </h1>
      </div>
    </>
  )
}

export default App
 
  return(
    <BrowserRouter>
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
        <Route path="/orders" element={<OrderHistory />} />
        <Route path="/tracker" element={<OrderTracker />} />
      </Routes>

    </BrowserRouter>
  )

  
}
export default App;
