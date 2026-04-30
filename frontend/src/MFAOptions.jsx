import { useState } from "react";
import { useNavigate } from "react-router-dom";

function MFAOptions() {
    const navigate = useNavigate();
    const [message, setMessage] = useState("");

    // 📱 TOTP
    const goToTOTP = () => {
        navigate("/setup-totp");
    };

    // 📩 SMS
    const enableSMS = async () => {
        const res = await fetch("http://127.0.0.1:8000/api/enable-sms-2fa/", {
            method: "POST",
            credentials: "include",
        });

        const data = await res.json();

        if (res.ok) {
            setMessage("SMS 2FA enabled");
        } else {
            setMessage(data.message || "Error enabling SMS");
        }
    };

    // ❌ Disable
    const disable2FA = async () => {
        const res = await fetch("http://127.0.0.1:8000/api/disable-2fa/", {
            method: "POST",
            credentials: "include",
        });

        const data = await res.json();

        if (res.ok) {
            setMessage("2FA disabled");
        } else {
            setMessage(data.message || "Error disabling 2FA");
        }
    };

    return (
        <div>
            <h2>Multi-Factor Authentication</h2>

            <button onClick={goToTOTP}>
                Use Authenticator App (e.g. Google Authenticator) (Recommended)
            </button>

            <br /><br />

            <button onClick={enableSMS}>
                Use SMS Code
            </button>

            <br /><br />

            <button onClick={disable2FA}>
                Disable 2FA
            </button>

            <br /><br />

            <button onClick={() => navigate("/settings")}>
                Back
            </button>

            {message && <p>{message}</p>}
        </div>
    );
}

export default MFAOptions;