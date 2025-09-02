 document.getElementById("loginForm").addEventListener("submit", function(e) {
    e.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const formData = new URLSearchParams();
    formData.append("username", username);
    formData.append("password", password);

    fetch("http://127.0.0.1:8000/auth/token", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.access_token) {
            localStorage.setItem("token", data.access_token);
            window.location.href = "index.html";
        } else {
            document.getElementById("error").textContent = "Login failed. Please check your credentials.";
        }
    })
    .catch(() => {
        document.getElementById("error").textContent = "An error occurred. Please try again.";
    });
});




