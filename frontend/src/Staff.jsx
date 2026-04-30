import { useNavigate } from "react-router-dom";

function Staff() {

    const navigate = useNavigate();

    const handleLogout = async () => {

        await fetch(
            "http://127.0.0.1:8000/api/logout/",
            {
                method: "POST",
                credentials: "include",
            }
        );

        navigate("/");

    };

    return (

        <div>

            <h1>Staff Dashboard</h1>

            <button onClick={handleLogout}>
                Logout
            </button>

        </div>

    );

}

export default Staff;