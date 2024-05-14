<?php

require_once("conexion.php");

function insertarRegistro()
{


//    echo 'Entro bien';

global $con;

$UserNombre= $_POST ['Unombre'];
$UserApellido= $_POST ['Uapellido'];
$UserDni= $_POST ['Udni'];
$UserFecha_nacimiento= $_POST ['Ufecha_nacimiento'];
$UserEmail= $_POST ['UEmail'];
$UserPassword= $_POST ['Upassword'];
$UserGenero= $_POST ['Ugenero'];
$UserCoche= $_POST ['Ucoche'];
$UserBici= $_POST ['Ubici'];
$UserAutos= $_POST ['Uautos'];


$query= "insert into form1 (Nombre, Apellido, Dni, Fecha_nacimiento, Email, Password, Genero, 
                                Coche, Bici, Autos) values ('$UserNombre', '$UserApellido', '$UserDni', 
                                str_to_date('$UserFecha_nacimiento', '%d/%m/%Y'), '$UserEmail', 
                                '$UserPassword', '$UserGenero', '$UserCoche', '$UserBici', '$UserAutos')";

$result= mysqli_query($con,$query);

        if($result)
        {
            echo ' El registro se creo exitosamente';
        }
        else
        {
            echo 'Por favor chequear la Query';
        }

}

?>
