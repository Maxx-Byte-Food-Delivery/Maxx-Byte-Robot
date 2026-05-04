export function showToast(message, positive) {

    const toast = document.createElement("div");
    toast.id = positive ? "snackbar" : "neg_snackbar";
    toast.className = "show";
    toast.innerText = message;

    document.body.appendChild(toast);

    setTimeout(() => {
        toast.className = toast.className.replace("show", "");
        document.body.removeChild(toast);
    }, 3000);
}