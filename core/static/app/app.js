//Validación de un formulario con Javascript
function valida_envia() {
 
  if (document.formu.nombre.value.length == 0) {
    alert("Tiene que escribir su nombre");
    document.formu.nombre.focus(); 
    return 0;
  }
  if (document.formu.correo.value.length == 0) {
    alert("Tiene que escribir su e-mail");
    document.formu.correo.focus();
    return 0;
  }
  telefono = document.formu.numero.value;
  if (telefono == "") {
    alert("Tiene que escribir su teléfono");
    document.formu.numero.focus();
    return 0;
   } 

  if (document.formu.mensaje.value.length == 0) {
    alert("Tiene que escribir su comentario");
    document.formu.mensaje.focus();
    return 0;
  }
  alert("Muchas gracias por enviar el formulario");
  document.formu.submit();
}
