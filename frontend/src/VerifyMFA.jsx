import { useState } from "react";
import axios from "axios";

function VerifyMFA() {

    const [token, setToken] = useState("");
    const username = localStorage.getItem("username");

    const handleSubmit = async (e) => {

        e.preventDefault();

        try {

            const response = await axios.post(
                "http://127.0.0.1:8000/api/verify-mfa/",
                {
                    username: username,
                    token: token
                }
            );

            alert(response.data.message);

            window.location.href = "/dashboard";

        } catch (error) {

            alert("Invalid MFA code");

        }

    };

    return (

        <form onSubmit={handleSubmit}>

            <h2>Enter MFA Code</h2>

            <input
                type="text"
                placeholder="Enter code"
                onChange={(e) =>
                    setToken(e.target.value)
                }
            />

            <button type="submit">
                Verify
            </button>

        </form>

    );

}

export default VerifyMFA;