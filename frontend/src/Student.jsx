import { useNavigate } from "react-router-dom";
import "./Student.css";

function Student() {

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

            {/* Top Bar */}
            <div className="top-bar">

                <button
                    className="top-button"
                    onClick={() =>
                        navigate("/settings")
                    }
                >
                    Settings
                </button>

                <button
                    className="top-button"
                    onClick={handleLogout}
                >
                    Logout
                </button>

            </div>

            {/* Page Content */}
            <div className="page-content">

                <h2>Student Dashboard</h2>

                <p>Welcome Student</p>

            </div>

        </div>

    );
}

export default Student;