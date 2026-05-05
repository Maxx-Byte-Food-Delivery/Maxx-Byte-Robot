import React, { useState } from "react";
import axios from "axios";
import { useLocation, useNavigate } from "react-router-dom";

const VerifyMFA = () => {

    const [code, setCode] = useState("");

    const location = useLocation();
    const navigate = useNavigate();

    const username = location.state?.username;
    const role = location.state?.role;

    const handleVerify = async (e) => {

        e.preventDefault();

        try {

            const response = await axios.post(
                "http://127.0.0.1:8000/api/verify-mfa/",
                {
                    username: username,
                    code: code
                }
            );

            if (role === "staff") {

                navigate("/staff");

            } else {

                navigate("/student");

            }

        }
        catch (error) {

            alert("Invalid or expired code");

        }

    };

    return (

        <form onSubmit={handleVerify}>

            <h2>Enter Code</h2>

            <input
                type="text"
                placeholder="Enter Code"
                value={code}
                onChange={(e) =>
                    setCode(e.target.value)
                }
            />

            <button type="submit">
                Verify
            </button>

        </form>

    );

};

export default VerifyMFA;