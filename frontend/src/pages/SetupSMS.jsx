import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import API from "../api/api";

function SetupSMS() {
    const [phone, setPhone] = useState("");
    const [profilePhone, setProfilePhone] = useState("");
    const [mode, setMode] = useState("existing");
    const [error, setError] = useState("");
    const navigate = useNavigate();

    useEffect(() => {
        const fetchProfile = async () => {
            try {
                const res = await API.get("/users/profile/");
                setProfilePhone(res.data.phone_number);
            } catch (err) {
                setError("Failed to load profile");
            }
        };

        fetchProfile();
    }, []);

    const handleSubmit = async (e) => {
        e.preventDefault();

        const phone_number =
            mode === "existing" ? profilePhone : phone;

        try {
            await API.post("/users/enable-sms-2fa/", {
                phone_number
            });

            navigate("/verify-sms");

        } catch (err) {
            setError(err.response?.data?.message || "Error");
        }
    };

    return (
        <div>
            <h2>Setup SMS Authentication</h2>

            {profilePhone && (
                <div>
                    <label>
                        <input
                            type="radio"
                            value="existing"
                            checked={mode === "existing"}
                            onChange={() => setMode("existing")}
                        />
                        Use existing number: {profilePhone}
                    </label>

                    <label>
                        <input
                            type="radio"
                            value="new"
                            checked={mode === "new"}
                            onChange={() => setMode("new")}
                        />
                        Use a new phone number
                    </label>
                </div>
            )}

            {mode === "new" && (
                <input
                    type="text"
                    placeholder="e.g. +15551234567"
                    value={phone}
                    onChange={(e) => setPhone(e.target.value)}
                />
            )}

            <button onClick={handleSubmit}>
                Send Code
            </button>

            {error && <p>{error}</p>}
        </div>
    );
}

export default SetupSMS;