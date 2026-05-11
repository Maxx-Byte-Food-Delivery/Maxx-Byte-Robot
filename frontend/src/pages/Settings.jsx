import { useNavigate } from "react-router-dom";

function Settings() {
    const navigate = useNavigate();

    return (
        <div>
            <h2>Settings</h2>

            <button onClick={() => navigate("/mfa-options")}>
                Enable/Disable Two Factor Authentication
            </button>

            <br /><br />

            <button onClick={() => navigate("/student")}>
                Back
            </button>
        </div>
    );
}

export default Settings;