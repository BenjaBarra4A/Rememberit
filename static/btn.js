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


document.getElementsByClassName('ver_contacto')[0].addEventListener('click', function() {
    document.getElementsByClassName('overlay_info')[0].style.display = 'block'; 
    document.getElementsByClassName('info_contacto_hidden')[0].style.display = 'block'; 
});

// Cerrar información del contacto al hacer clic en el botón "Cerrar"
document.getElementsByClassName('cerrar_info')[0].addEventListener('click', function() {
    document.getElementsByClassName('overlay_info')[0].style.display = 'none'; 
    document.getElementsByClassName('info_contacto_hidden')[0].style.display = 'none'; 
});

// Cerrar información del contacto al hacer clic fuera del contenido (overlay)
document.getElementsByClassName('overlay_info')[0].addEventListener('click', function() {
    this.style.display = 'none'; 
    document.getElementsByClassName('info_contacto_hidden')[0].style.display = 'none'; 
});

//______________________________________________________________________________________________

// APARACER FORM EDITAR CONTATO

document.getElementById('editar_contacto').addEventListener('click', function() {
    document.getElementById('overlay_editar').style.display = 'block'; 
    document.getElementById('editar_contacto_hidden').style.display = 'block'; 
});

document.getElementById('cerrar_editar').addEventListener('click', function() {
    document.getElementById('overlay_editar').style.display = 'none'; 
    document.getElementById('editar_contacto_hidden').style.display = 'none'; 
});

document.getElementById('overlay_editar').addEventListener('click', function() {
    this.style.display = 'none'; 
    document.getElementById('editar_contacto_hidden').style.display = 'none'; 
    
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


