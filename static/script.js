document.addEventListener("DOMContentLoaded", () => {
    fetch("/api")
        .then(res => res.json())
        .then(data => {
            const msg = d ocument.createElement("p");
            msg.innerText = data.message;
            document.body.appendChild(msg);
        });
});