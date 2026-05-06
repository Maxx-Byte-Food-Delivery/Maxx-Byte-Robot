import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "./api";

function ConfirmTOTP() {
    const navigate = useNavigate();
    const [code, setCode] = useState("");
    const [error, setError] = useState("");

    const confirm = async () => {
        try {
            const res = await API.post("/confirm-totp/", {
                code: code,
            });

            alert("TOTP enabled!");
            navigate("/student"); // ✅ redirect properly

        } catch (err) {
            setError("Invalid code");
        }
    };

    return (
        <div>
            <h2>Confirm Authenticator</h2>

            <input
                type="text"
                placeholder="Enter code from app"
                value={code}
                onChange={(e) => setCode(e.target.value)}
            />

            <button onClick={confirm}>Confirm</button>

            {error && <p style={{ color: "red" }}>{error}</p>}
        </div>
    );
}

export default ConfirmTOTP;