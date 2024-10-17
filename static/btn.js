//NAVBAR

document.addEventListener("DOMContentLoaded", function() {
    const cambiarbtn = document.querySelector(".cambiar_btn");
    const navbar = document.querySelector(".navbar-hiden");

    if (cambiarbtn && navbar) { 
        cambiarbtn.onclick = function() {
            navbar.classList.toggle("open");
            console.log(cambiarbtn); 
            console.log(navbar); 
        }
    }
});

//_____________________________________________________________________________________________

// APARECE FORM CREAR CONTACTO

document.getElementById('openFormButton').addEventListener('click', function() {
    document.getElementById('overlay').style.display = 'block'; 
    document.getElementById('contactForm').style.display = 'block'; 
});
//_____________________________________________________________________________________________
// APARECE INFORMACION DE LOS USUARIOS

// Función para mostrar la información del contacto
document.querySelectorAll('.ver_contacto').forEach(button => {
    button.addEventListener('click', function() {
        const contactoId = this.closest('.cubo').id.split('_')[1]; // Obtener el ID del contacto
        document.getElementById(`overlay_info_${contactoId}`).style.display = 'block'; 
        document.getElementById(`info_contacto_${contactoId}`).style.display = 'block'; 
    });
});

// Cerrar información del contacto al hacer clic en el botón "Cerrar"
document.querySelectorAll('.cerrar_info').forEach(button => {
    button.addEventListener('click', function() {
        const contactoId = this.closest('.info_contacto_hidden').id.split('_')[1]; // Obtener el ID del contacto
        document.getElementById(`overlay_info_${contactoId}`).style.display = 'none'; 
        document.getElementById(`info_contacto_${contactoId}`).style.display = 'none'; 
    });
});

// Cerrar información del contacto al hacer clic fuera del contenido (overlay)
document.querySelectorAll('.overlay_info').forEach(overlay => {
    overlay.addEventListener('click', function() {
        const contactoId = this.id.split('_')[1]; // Obtener el ID del contacto
        this.style.display = 'none'; 
        document.getElementById(`info_contacto_${contactoId}`).style.display = 'none'; 
    });
});

// APARECER FORM EDITAR CONTACTO
document.querySelectorAll('.editar_contacto').forEach(button => {
    button.addEventListener('click', function() {
        const contactoId = this.closest('.cubo').id.split('_')[1]; // Obtener el ID del contacto
        document.getElementById(`overlay_editar_${contactoId}`).style.display = 'block'; 
        document.getElementById(`editar_contacto_hidden_${contactoId}`).style.display = 'block'; 
    });
});

// Cerrar edición del contacto
document.querySelectorAll('.cerrar_editar').forEach(button => {
    button.addEventListener('click', function() {
        const contactoId = this.getAttribute('data-id'); // Obtener el ID del contacto
        document.getElementById(`overlay_editar_${contactoId}`).style.display = 'none'; 
        document.getElementById(`editar_contacto_hidden_${contactoId}`).style.display = 'none'; 
    });
});

// Cerrar edición del contacto al hacer clic fuera del contenido (overlay)
document.querySelectorAll('.overlay_editar').forEach(overlay => {
    overlay.addEventListener('click', function() {
        const contactoId = this.id.split('_')[1]; // Obtener el ID del contacto
        this.style.display = 'none'; 
        document.getElementById(`editar_contacto_hidden_${contactoId}`).style.display = 'none'; 
    });
});
//______________________________________________________________________________________

document.addEventListener("DOMContentLoaded", function() {
    const today = new Date(); 
    const day = String(today.getDate()).padStart(2, '0'); 
    const month = String(today.getMonth() + 1).padStart(2, '0'); 
    const year = today.getFullYear(); // Año

    const formattedDate = `${year}-${month}-${day}`; 

  
    const fechaInput = document.getElementById("fecha");
    fechaInput.setAttribute("min", formattedDate); 
});


