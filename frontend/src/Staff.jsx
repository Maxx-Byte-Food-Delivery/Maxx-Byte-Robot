import { useNavigate } from "react-router-dom";

function Staff() {

    const navigate = useNavigate();

    const handleLogout = async () => {

        await fetch(
            "http://localhost:8000/api/logout/",
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