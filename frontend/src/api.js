import axios from "axios";

// ✅ Create axios instance
const API = axios.create({
    baseURL: "http://localhost:8000/api",
    withCredentials: true, // always send cookies
});

// ✅ Get CSRF token from cookie
const getCSRFToken = () => {
    return document.cookie
        .split("; ")
        .find(row => row.startsWith("csrftoken"))
        ?.split("=")[1];
};

// ✅ Attach CSRF token automatically to unsafe requests
API.interceptors.request.use((config) => {
    const csrfToken = getCSRFToken();

    // Only attach for methods that need CSRF
    if (
        ["post", "put", "patch", "delete"].includes(
            config.method?.toLowerCase()
        )
    ) {
        if (csrfToken) {
            config.headers["X-CSRFToken"] = csrfToken;
        }
    }

    return config;
});

export default API;