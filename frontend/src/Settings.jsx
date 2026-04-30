import { useState } from "react";

function Settings({ setPage }) {
    const [message, setMessage] = useState("");

    // 🔐 Enable TOTP (go to QR setup)
    const enableTOTP = () => {
        setPage("setup-totp");
    };

    // 📩 Enable SMS
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

    // ❌ Disable 2FA
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
            <h2>Settings</h2>

            <button onClick={enableTOTP}>
                Enable Authenticator App (TOTP)
            </button>

            <br /><br />

            <button onClick={enableSMS}>
                Enable SMS 2FA
            </button>

            <br /><br />

            <button onClick={disable2FA}>
                Disable 2FA
            </button>

            <br /><br />

            <button onClick={() => setPage("student")}>
                Back
            </button>

            {message && <p>{message}</p>}
        </div>
    );
}

export default Settings;