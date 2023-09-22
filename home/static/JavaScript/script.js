function mostrar(id) {
    if (id == "ida") {
        $("#ida").show();
        $("#idayvuelta").hide();
        $("#puntoapunto").hide();
    }

    if (id == "idayvuelta") {
        $("#ida").hide();
        $("#idayvuelta").show();
        $("#puntoapunto").hide();
    }

    if (id == "puntoapunto") {
        $("#ida").hide();
        $("#idayvuelta").hide();
        $("#puntoapunto").show();
    }

}

function mostrarContenido(numeroContenido) {
    // Ocultar todos los contenidos
    // document.getElementById('contenido1').style.display = 'none';
    // document.getElementById('contenido2').style.display = 'none';
  
    // Mostrar el contenido seleccionado
    document.getElementById('contenido1').style.display = 'none';
    document.getElementById('contenido2').style.display = 'none';

    document.getElementById(`contenido${numeroContenido}`).style.display = 'block';

    if (numeroContenido == 1) {
        alert("Esta en ida")
    } else if (numeroContenido == 2) {
        alert("Esta en vuelta");
    } else {
        alert("NO ESTA FUNCIONANDO BIEN")
    }
};

// function mostrarContenido(numeroContenido) {
//     // Ocultar todos los contenidos
//     document.getElementById('contenido1').style.display = 'none';
//     document.getElementById('contenido2').style.display = 'none';

//     // Mostrar el contenido seleccionado
//     document.getElementById(`contenido${numeroContenido}`).style.display = 'block';

//     // Desactivar todos los botones
//     document.querySelectorAll('button').forEach(function(btn) {
//         btn.disabled = true;
//     });

//     // Reactivar el botón seleccionado
//     document.querySelector(`button:nth-child(${numeroContenido + 1})`).disabled = false;
// }
  