import { useState } from "react";

function ConfirmTOTP({ setPage }) {
    const [code, setCode] = useState("");
    const [error, setError] = useState("");

    const confirm = async () => {
        const res = await fetch("http://127.0.0.1:8000/api/confirm-totp/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            credentials: "include",
            body: JSON.stringify({ code }),
        });

        const data = await res.json();

        if (res.ok) {
            alert("TOTP enabled!");
            setPage("student");
        } else {
            setError(data.message || "Invalid code");
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