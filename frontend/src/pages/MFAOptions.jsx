import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import API from "../api/api";

function MFAOptions() {
    const navigate = useNavigate();

    const [profile, setProfile] = useState(null);
    const [message, setMessage] = useState("");

    // 🔍 Load MFA status
    useEffect(() => {
        const fetchProfile = async () => {
            try {
                const res = await API.get("/users/profile/");
                setProfile(res.data);
            } catch (err) {
                if (err.response?.status === 401) {
                    navigate("/");
                } else {
                    console.error(err);
                }
            }
        };

        fetchProfile();
    }, []);

    if (!profile) return <p>Loading...</p>;

    return (
        <div style={{ padding: "20px" }}>

            <h2>Multi-Factor Authentication</h2>

            {/* 📊 Current status */}
            <p>
                Status:{" "}
                {profile.mfa_enabled
                    ? `Enabled (${profile.mfa_method?.toUpperCase()})`
                    : "Disabled"}
            </p>

            <hr />

            {/* 🔐 Options */}
            <h3>Choose a method</h3>

            <button onClick={() => navigate("/setup-totp")}>
                🔑 Use Authenticator App (TOTP)
            </button>

            <br /><br />

            <button onClick={() => navigate("/setup-sms")}>
                📱 Use SMS Code
            </button>

            <br /><br />

            {profile.mfa_enabled && (
                <button
                    onClick={async () => {
                        try {
                            await API.post("/users/disable-2fa/");
                            setProfile({
                                ...profile,
                                mfa_enabled: false,
                                mfa_method: null
                            });
                            setMessage("2FA disabled");
                        } catch (err) {
                            setMessage(err.response?.data?.message || "Error");
                        }
                    }}
                >
                    ❌ Disable 2FA
                </button>
            )}

            <br /><br />

            {/* 🔙 Back */}
            <button onClick={() => navigate("/settings")}>
                Back
            </button>

            {/* 📢 Messages */}
            {message && <p>{message}</p>}
        </div>
    );
}

export default MFAOptions;