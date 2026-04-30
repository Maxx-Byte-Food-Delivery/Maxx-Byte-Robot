import { useNavigate } from "react-router-dom";

function Settings() {

    const navigate = useNavigate();

    const enableMFA = () => {

        window.location.href =
            "http://127.0.0.1:8000/account/two_factor/setup/";

    };

    return (

        <div>

            <h2>Settings</h2>

            <button onClick={enableMFA}>
                Enable MFA
            </button>

            <br /><br />

            <button onClick={() =>
                navigate("/staff")
            }>
                Back
            </button>

        </div>

    );
}

export default Settings;