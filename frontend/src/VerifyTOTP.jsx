import { useState } from "react";

function VerifyTOTP({ setPage }) {
    const [code, setCode] = useState("");
    const [error, setError] = useState("");

    const verify = async () => {
        const res = await fetch("http://127.0.0.1:8000/api/verify-2fa/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ code }),
        });

        const data = await res.json();

        if (res.ok) {
            if (data.role === "staff") setPage("staff");
            else navigate("/student");
        } else {
            setError(data.message || "Invalid code");
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