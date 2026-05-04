import { useState } from "react";

function SetupTOTP({ setPage }) {
    const [qr, setQr] = useState("");
    const [loading, setLoading] = useState(false);

    const generateQR = async () => {
        setLoading(true);

        const res = await fetch("http://localhost:8000/api/setup-totp/", {
            method: "POST",
            credentials: "include",
        });

        const data = await res.json();

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

                    <button onClick={() => setPage("confirm-totp")}>
                        Next
                    </button>
                </>
            )}
        </div>
    );
}

export default SetupTOTP;