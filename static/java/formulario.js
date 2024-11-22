
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






const fechaInput = document.getElementById("fecha");
const horaInput = document.getElementById("hora");

// cada vez que haya un cambio en esa fecha o hora
fechaInput.addEventListener("change", verificarDisponibilidad);
horaInput.addEventListener("change", verificarDisponibilidad);

function verificarDisponibilidad() {
    const fecha = fechaInput.value;
    const hora = horaInput.value;

    if (fecha && hora) { // si ambos campos tienen valor
        fetch(`/verificar-disponibilidad/?fecha=${fecha}&hora=${hora}`) // envia una solicitud http get al servidor , usando esa url
            .then(response => response.json()) // Convertir la respuesta a json(java) a un objeto , ya que venia entre "" y asi se puede acceder a los datos como un diccionario
            .then(data => {
                if (data.disponible) { // la variable que nos pasanes disponible = true o false
                    alert("¡Hay espacio disponible!");
                } else {
                    alert("No hay espacio para esa fecha y hora.");
                }
            })
            .catch(error => {
                console.error("Error:", error);
                alert("Hubo un error al verificar la disponibilidad.");
            });
    }
}

