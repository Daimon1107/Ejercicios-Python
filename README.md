# Ejercicios-Python

Diferentes ejercicios de python 

#EJERCICIO 1


En una tienda de reparación de computadores el dueño de la empresa necesita un sistema que le permita ingresar los datos del cliente o equipo y realizar búsquedas. Crear un programa con un menú de 3 opciones: 1. Buscar información, 2. Ingresar nueva Información3. Salir.

En la opción de Ingresar se deberá ir creando en registro la siguiente información: Nombre, Apellido, Marca de computador, Ciudad de residencia del cliente, tamaño del computador (en pulgadas).

En la función Buscar, se debe pedir al usuario que ingrese un parámetro para ingresar ya sea (nombre, apellido, marca del computador, ciudad de residencia, tamaño). El resultado de la búsqueda deberá ser todo el registro del cliente que coincida con el parámetro ingresado.

El menú principal debe repetirse hasta que el usuario seleccione la opción Salir.

Ejemplo:

Cliente1: Maria, Acosta, HP, Quito, 14

Cliente 2: Juan, Bautista,lenovo,Pelileo,13

Cliente 3: Fernando, Gavilanes, HP, 13

Cliente 4: Maria, Solis, hacer, Ambato,15

Parámetro de búsqueda: 13

Resultado:

               Cliente 2: Juan, Bautista, Lenovo, Pelileo,13

Cliente 3: Fernando, Gavilanes, HP, 13

Parámetro de búsqueda: Maria

Resultado:

               Cliente1: Maria, Acosta, HP, Quito, 14

               Cliente 4: Maria, Solis, hacer, Ambato,15



#EJERCICIO 3

Realizar un programa para ingresar por teclado  listas dentro de una lista principal con los datos de 4  mascotas de un hospital. 
Los datos serán:

  - Nombre  (tipo de dato str)
  - Edad (tipo de dato int)
  - True / False (tipo booleano) (True para vacunas al día, False sin vacunas
  - Peso (tipo float) en kg
  
Los parámetros son ingresados en cualquier orden, por ejemplo

	Hospital_Veterinario=[[‘Roky’, True ,10.5 , 3], [5, ’Luna’, False, 5.4],[False, 4.8, ‘Firulais’, 2],[3, 12.5 , ‘Quesito’, True]]

Una vez que se termine de llenar la información, debe devolver la lista con los datos ordenados por:

1. edad 2. Nombre 3. Peso 4. Vacunas
  
Se imprimirá la lista con los elementos de la lista anterior que deben estar ordenados desde la mascota con mayor edad hasta la de menor edad

Ejemplo:

	resultado=[[5, ’Luna’, 5.4, False],[3, ‘Roky’, 10.5 , True], [3, ‘Quesito’, 12.5 , True], [2, ‘Firulais’, 8.4, False]]
  
  



