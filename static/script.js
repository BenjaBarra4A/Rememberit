window.addEventListener('load', function() {
    var correoGuardado = localStorage.getItem("email");
    var contraseñaGuardada = localStorage.getItem("password");

    // Si ya existen datos guardados, rellenar los campos
    if (correoGuardado && contraseñaGuardada) {
        document.getElementById("email").value = correoGuardado;
        document.getElementById("password").value = contraseñaGuardada;
    }

    // Preguntar al usuario si desea guardar la sesión (correo y contraseña)
    var quiereGuardarSesion = confirm("¿Deseas recordar tu correo y contraseña para la próxima sesión?");

    if (quiereGuardarSesion) {
        var recordar = document.getElementById("recordar");
        
        // Añadir evento click al botón para guardar los datos
        recordar.addEventListener("click", function() {
            // Obtener los valores del correo y la contraseña desde los inputs
            var correo = document.getElementById("email").value;
            var contraseña = document.getElementById("password").value;

            if (correo && contraseña) {
                // Guardar el correo y la contraseña en localStorage
                localStorage.setItem("email", correo);
                localStorage.setItem("password", contraseña);

                // Mostrar alerta de éxito
                alert('Correo y contraseña guardados correctamente');
            } else {
                // Mostrar alerta de error si los campos están vacíos
                alert('Por favor, completa ambos campos.');
            }
        });
    } else {
        // Si el usuario no desea recordar la sesión, borrar cualquier dato guardado
        localStorage.removeItem("email");
        localStorage.removeItem("password");
    }
});