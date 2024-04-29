<?php
                $servername = "localhost";
                $username = "root";
                $password = ""; // Deja esto en blanco si no has configurado una contraseña
                $dbname = "regresion_lineal"; // Reemplaza esto con el nombre de tu base de datos

    // Crear conexión
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Verificar la conexión
    if ($conn->connect_error) {
        die("Conexión fallida: " . $conn->connect_error);
    }

        // Ejecutar la consulta
        $query = "SELECT edad, genero, calificacion FROM usuarios
        INNER JOIN preferencias ON usuarios.id = preferencias.usuario_id"; 


        $result = $conn->query($query);

        //si sale un error alterno en la consulta 

        if (!$result) {
            die("Error en la consulta: " . $conn->error);
        }
       
        //si sale todo perfecto entonces se almacenara todos los datos en una array para luego usarlos 
          
        $data = array();

        if ($result->num_rows > 0) {
            // Guardar los resultados en un array
            while ($row = $result->fetch_assoc()) {
                $data[] = array($row["edad"], ($row["genero"] === 'Masculino' ? 1 : 0), $row["calificacion"]);
            }
        } else {
            echo "0 resultados";
        }

    // Cerrar conexión
    $conn->close();

    // Devolver los resultados como JSON
    echo json_encode($data);
?>