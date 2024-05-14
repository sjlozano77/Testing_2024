// evento btn registro
$(document).ready(function() {

//alert('prueba funciones');

Insertar_registro();
//Mostrar_registro();
//Obtener_registro();
//Agregar_registro();
//Eliminar_registro();

})

function Insertar_registro() {

$(document).on('click','#enviar',function() {

    var nombre = $('#nombre').val();
    var apellido = $('#apellido').val();
    var dni = $('#dni').val();
    var fecha_nacimiento = $('#fecha_nacimiento').val();
    var email = $('#email').val();
    var password = $('#password').val();
    var genero = $('#genero').val();
    var coche = $('#coche').val();
    var bici = $('#bici').val();
    var autos = $('#autos').val();
    
    
    //validacion frontend

    if (User == "" || Email == "") 
    {

        $('#message').html('llenar los campos');

    }
    else
    {
        $ajax({
            URL: 'Insertar.php',
            method: 'post',
            data: {UName:Nombre, UApellido:apellido, UDni:dni, UFecha_nacimiento:fecha_nacimiento, 
                   UEmail:Email, UPasswors:password, UGenero:genero, UCoche:coche, UBici:bici, 
                   UAutos:Auto},
            success: function(data)
            {
                $('#message').html(data);
                //$('#Registration').modal('show');
                //$('form').trigger('reset');
                //Mostrar_registro();

                alert("Entro a la funcion");
                alert(data);
            }

        })
    }
})
}
