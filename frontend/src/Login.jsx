import React, { useEffect, useState } from "react";
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Login = () =>{
  const navigate = useNavigate();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');


  const handleLogin = async (e) =>{
    e.preventDefault();

    try {
        const response = await axios.post(
            "http://127.0.0.1:8000/api/users/login/",
            {
                username: username,
                password: password,
            }
        );
        //setMessage(response.data.message);
        
        alert(response.data.message);
        
        navigate("/page");

    }   catch (error) {

        setMessage(
            "Invalid username or password"
        );
    }
  }

  return (

    <div style={styles.container}>

      <form
        onSubmit={handleLogin}
        style={styles.box}
      >

        <h2>Login</h2>

        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) =>
            setUsername(e.target.value)
          }
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) =>
            setPassword(e.target.value)
          }
        />

        <button type="submit">
          Login
        </button>

        <p>{message}</p>

      </form>

    </div>
  );
}

const styles = {

  container: {
    height: "100vh",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
  },

  box: {
    width: "300px",
    padding: "20px",
    border: "1px solid #ccc",
    borderRadius: "8px",
  }

};

export default Login;