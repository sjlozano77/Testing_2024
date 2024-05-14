function validacion()
{
    var  nombre = document.getElementById("nombre").value;
    var  apellido = document.getElementById("apellido").value;
    var  dni = document.getElementById("dni").value;
    var  fecha_nacimiento = document.getElementById("fecha_nacimiento").value;
    var email = document.getElementById( "email" ).value;
    var password = document.getElementById( "password" ).value;
    const genero = document.querySelectorAll('input[name="genero"]');
    const vehiculo = document.querySelectorAll('input[name="vehiculo"]');
    const autos = document.querySelectorAll('input[name="autos"]');
    var resultado;
    console.log("entro");
    //Validación de que el email este completo
    alert(nombre + " " + apellido);
   
    if (nombre == "" || apellido == "" || email =="") {
      const nombreError = document.getElementById("nombreError");
      nombreError.removeAttribute("hidden");
      //alert ("Todos los campos son obligatorios");
        //return false;
    } else {
      //alert('Los datos ingresados son correctos');    
      //return true;
    }
      //console.log(validateEmail("javier@g,ail.com"));
    if(validateEmail())
        {
            alert('El mail esta correcto');                
        }
        else
        {
            alert('el mail no esta correcto');    
        }
      if(vehiculo.checked)
      {
          alert('Los datos ingresados son correctos');    
          }
          else
          {
              alert ('Debe seleccionar una opción en el campo Vehículo') ;  
          }
     
   
      return true;    
}
