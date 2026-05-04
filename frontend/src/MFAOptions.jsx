import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { getCSRF } from "/src/utils/csrf";

function MFAOptions() {
    const navigate = useNavigate();

    const [profile, setProfile] = useState(null);
    const [showOptions, setShowOptions] = useState(false);
    const [message, setMessage] = useState("");

    // 🔍 Load current MFA status
    useEffect(() => {
        fetch("http://127.0.0.1:8000/api/user-profile/", {
            credentials: "include",
            headers: {
                "X-CSRFToken": getCSRF(),
            }
        })
            .then(res => {
                if (res.status === 401) {
                    navigate("/"); // 🚨 send back to login
                    return null;
                }
                return res.json();
            })
            .then(data => {
                if (data) setProfile(data);
            })
            .catch(err => console.error(err));
    }, []);

    // 📱 Switch to TOTP
    const switchToTOTP = () => {
        navigate("/setup-totp");
    };

    // 📩 Switch to SMS
    const switchToSMS = async () => {
        const res = await fetch("http://127.0.0.1:8000/api/enable-sms-2fa/", {
            method: "POST",
            credentials: "include",
            headers: {
                "X-CSRFToken": getCSRF(),
            }
        });

        const data = await res.json();

        if (res.ok) {
            setMessage("Switched to SMS 2FA");
            setProfile({ ...profile, mfa_enabled: true, mfa_method: "sms" });
            setShowOptions(false);
        } else {
            setMessage(data.message || "Error");
        }
    };

    // ❌ Disable
    const disable2FA = async () => {
        const res = await fetch("http://127.0.0.1:8000/api/disable-2fa/", {
            method: "POST",
            credentials: "include",
            headers: {
                "X-CSRFToken": getCSRF(),
            }
        });

        const data = await res.json();

        if (res.ok) {
            setMessage("2FA disabled");
            setProfile({ ...profile, mfa_enabled: false, mfa_method: null });
            setShowOptions(false);
        } else {
            setMessage(data.message || "Error");
        }
    };

    if (!profile) return <p>Loading...</p>;

    return (
        <div>
            <h2>Multi-Factor Authentication</h2>

            {/* 🔐 Current status */}
            <p>
                Status:{" "}
                {profile.mfa_enabled
                    ? `Enabled (${profile.mfa_method?.toUpperCase()})`
                    : "Disabled"}
            </p>

            <br />

            {/* 🔁 Change method */}
            <button onClick={() => setShowOptions(!showOptions)}>
                Change Method
            </button>

            <br /><br />

            {showOptions && (
                <div>
                    <button onClick={switchToTOTP}>
                        Use Authenticator App (Recommended)
                    </button>

                    <br /><br />

                    <button onClick={switchToSMS}>
                        Use SMS Code
                    </button>

                    <br /><br />

                    {profile.mfa_enabled && (
                        <>
                            <button onClick={disable2FA}>
                                Disable 2FA
                            </button>

                            <br /><br />
                        </>
                    )}
                </div>
            )}

            <br /><br />

            <button onClick={() => navigate("/settings")}>
                Back
            </button>

            {message && <p>{message}</p>}
        </div>
    );
}

export default MFAOptions;