function requestNotificationPermission() {
    if ("Notification" in window) {
        Notification.requestPermission().then(function (permission) {
            if (permission === "granted") {
                console.log("Permiso de notificaciones concedido");
            } else {
                console.log("Permiso de notificaciones denegado");
            }
        });
    } else {
        alert("Este navegador no soporta notificaciones de escritorio.");
    }
}