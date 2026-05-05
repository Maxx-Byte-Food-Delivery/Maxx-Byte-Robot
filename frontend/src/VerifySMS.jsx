import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import API from "./api";

function VerifySMS() {
    const [code, setCode] = useState("");
    const [error, setError] = useState("");
    const [cooldown, setCooldown] = useState(0);
    const navigate = useNavigate();

    const verify = async () => {
        try {
            const res = await API.post("/verify-sms/", {
                code: code.trim(),
            });

            const data = res.data;

            navigate(data.role === "staff" ? "/staff" : "/student");

        } catch (err) {
            setError("Invalid code");
        }
    };

    const resend = async () => {
        try {
            await API.get("/verify-sms/");
            setCooldown(30);
        } catch {
            setError("Failed to resend code");
        }
    };

    useEffect(() => {
        if (cooldown <= 0) return;

        const timer = setInterval(() => {
            setCooldown((prev) => prev - 1);
        }, 1000);

        return () => clearInterval(timer);
    }, [cooldown]);

    return (
        <div>
            <h2>Enter SMS Code</h2>

            <input
                type="text"
                placeholder="6-digit code"
                value={code}
                onChange={(e) => setCode(e.target.value)}
            />

            <button onClick={verify}>Verify</button>

            <br /><br />

            <button onClick={resend} disabled={cooldown > 0}>
                {cooldown > 0 ? `Resend in ${cooldown}s` : "Resend Code"}
            </button>

            {error && <p style={{ color: "red" }}>{error}</p>}
        </div>
    );
}

export default VerifySMS;