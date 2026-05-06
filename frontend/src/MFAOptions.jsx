import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import API from "./api";

function MFAOptions() {
    const navigate = useNavigate();

    const [profile, setProfile] = useState(null);
    const [showOptions, setShowOptions] = useState(false);
    const [message, setMessage] = useState("");

    // 🔍 Load current MFA status
    useEffect(() => {
        const fetchProfile = async () => {
            try {
                const res = await API.get("/user-profile/");
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

    // 📱 Switch to TOTP
    const switchToTOTP = () => {
        navigate("/setup-totp");
    };

    // 📩 Switch to SMS
    const switchToSMS = async () => {
        try {
            const res = await API.post("/enable-sms-2fa/");

            navigate("/verify-sms");

        } catch (err) {
            setMessage(err.response?.data?.message || "Error");
        }
    };

    // ❌ Disable
    const disable2FA = async () => {
        try {
            const res = await API.post("/disable-2fa/");

            setMessage("2FA disabled");
            setProfile({ ...profile, mfa_enabled: false, mfa_method: null });
            setShowOptions(false);

        } catch (err) {
            setMessage(err.response?.data?.message || "Error");
        }
    };

    if (!profile) return <p>Loading...</p>;

    return (
        <div>
            <h2>Multi-Factor Authentication</h2>

            <p>
                Status:{" "}
                {profile.mfa_enabled
                    ? `Enabled (${profile.mfa_method?.toUpperCase()})`
                    : "Disabled"}
            </p>

            <br />

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