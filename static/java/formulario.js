
var formulario = document.getElementById("form");
formulario.addEventListener("submit", function (event) {
      
    var nombre = document.getElementById("nombre").value;
    var hora = document.getElementById("hora").value;
    var fecha = document.getElementById("fecha").value;

    alert(`Formulario enviado con éxito. Gracias por tu reserva, ${nombre}.
Recuerda que tu reserva es el ${fecha} a las ${hora}. ¡Te esperamos!`);
});


document.getElementById("email").addEventListener("input", function () {
    const email = this.value;  // aqui tengo el valor del email
   
    // Expresión regular para validar correos electrónicos
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const mensaje = document.getElementById("mensaje-email");

    if (emailRegex.test(email)) { // esto se utiliza para verificar que la cadena de texto cumple
        mensaje.textContent = "El correo es válido.";
        mensaje.style.color = "green";
    } else {
        mensaje.textContent = "El correo no es válido.";
        mensaje.style.color = "red";
    }
});


