import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "./api";

function SetupTOTP({ setPage }) {
    const [qr, setQr] = useState("");
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const generateQR = async () => {
        setLoading(true);

        const res = await API.post("/setup-totp/");
        const data = res.data;

        setQr(data.qr_code);
        setLoading(false);
    };

    return (
        <div>
            <h2>Setup Authenticator</h2>

            <button onClick={generateQR}>Generate QR Code</button>

            {loading && <p>Loading...</p>}

            {qr && (
                <>
                    <p>Scan this with Google Authenticator</p>
                    <img src={`data:image/png;base64,${qr}`} alt="QR Code" />

                    <button onClick={() => navigate("/confirm-totp")}>
                        Next
                    </button>
                </>
            )}
        </div>
    );
}

export default SetupTOTP;