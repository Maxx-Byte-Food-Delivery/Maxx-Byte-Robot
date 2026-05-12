import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../api/api";

function SetupSMS() {
    const [phone, setPhone] = useState("");
    const [error, setError] = useState("");
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            await API.post("/users/enable-sms-2fa/", {
                phone_number: phone
            });

            navigate("/verify-sms");

        } catch (err) {
            setError(err.response?.data?.message || "Error");
        }
    };

    return (
        <div>
            <h2>Setup SMS Authentication</h2>

            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="e.g. +15551234567"
                    value={phone}
                    onChange={(e) => setPhone(e.target.value)}
                />

                <button type="submit">
                    Send Code
                </button>
            </form>

            {error && <p>{error}</p>}
        </div>
    );
}

export default SetupSMS;