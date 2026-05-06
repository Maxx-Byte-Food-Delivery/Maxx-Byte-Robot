import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "./api";

function VerifyTOTP() {
    const [code, setCode] = useState("");
    const [error, setError] = useState("");
    const navigate = useNavigate();

    const verify = async () => {
        try {
            const res = await API.post("/confirm-totp/", {
                code: code.trim(),
            });

            const data = res.data;

            // Redirect based on role
            if (data.role === "staff") {
                navigate("/staff");
            } else {
                navigate("/student");
            }

        } catch (err) {
            setError("Invalid code");
        }
    };

    return (
        <div>
            <h2>Enter Authenticator Code</h2>

            <input
                type="text"
                placeholder="6-digit code"
                value={code}
                onChange={(e) => setCode(e.target.value)}
            />

            <button onClick={verify}>Verify</button>

            {error && <p style={{ color: "red" }}>{error}</p>}
        </div>
    );
}

export default VerifyTOTP;