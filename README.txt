--------------------------------------EXPLICACION DE LOS ARCHIVOS--------------------------------------------------
classes.py
Este archivo contiene los objetos principales del proyecto contiene las clases:
-Subject: Representa una asignatura

-Student: Representa el estudiante con su lista de materis solicitadas y la de materias asiganas inicialmente vacia
tambien tiene algunas funciones para cualcula su insatisfaccion y para asignarle una materia

-SoliciteSubject: Representa la solicitud de una materia con su prioridad


brute_force.py
Clase que contiene las funciones que componen el algoritmo exhaustivo

voraz.py
Clase que contiene las funciones que componen el algoritmo voraz

dinamic_and_recursive.py
Clase que contiene la implentacion dinamica con memoization esta ultima fue la
que se uso para el algoritmo dinamico

load_data.py
Esta clase es la que contiene todas las funciones que procesan las entradas de texto plano en el formato del proyecto y las convierte 
en objetos utilizables por las clases de los algoritmos

capeta inputs
esta carpeta contiene todo los archivos de entradas, de aqui es donde lee los datos load_data.py

write_data.py 
Funcion que toma la salida de los algoritmos la procesa y la escribe en el formato de salida dentro de una carpeta llamada "outputs" y 
guarda el archivo en formato txt con el siguiente nombre: "salida_<nombre del algoritmo que se ejecuto>_<nombre de la entrada que se ejecuto>.txt"
Ejemplo: si ejecuta el algoritmo voraz con un archivo txt llamado test_1.txt el archivo guardado en la carpeta "outputs" debera llamarse:
"salida_voraz_test_1.txt"

carpeta outputs
En esta carpeta es donde es guardan los archivos de los tests escritos por la clase write_data.py

controller.py
Esta es la clase controladora del programa la cual llamada a las demas clases menciondas antes, funciona como pipeline que ejecuta las 
funciones nesesarias para correr los algoritmos y tambien escribe las soluciones en los txt

App.py
Esta es una GUI amigable que permite cargar todos los archivos de prueba y ejecutarlos en una interfaz amigable y simple. para ejecutarla 
correr "python App.py". Es la primera opcion de ejecucion de la aplicacion que debe considerar el usuario.

view.py 
Esta es una interfaz adicional que se realizo para utilizar la linea de comandos como interfaz para correr la aplicacion,
Esta interfaz es mas simple, pero a la vez mais intuitiva y sensilla. Es opcional por si la interfaz grafica llega a fallar por
algun motivo imprevisto. Para usarla utilizar el comando "python main.py "

main.py 
En este archivo se ejecuta la interfaz de consola. (utilizar la interfaz de consola como segunda opcion)


-----------------------------INSTRUCCIONES DE USO--------------------------------------------------------------------------------
-Ponga en la carpeta inputs los archivos de entrada que se quiera probar, luego ejecute el archivo "python App.py" (opcional ejecute "python main.py") esto desplegar un menu
en una GUI. 

-primero le pedira elegir un archivo de entrada para ejecutar los algoritmo, tenga en cuenta que el archivo debe estar en la carpeta 
inputs antes de seleccionarlo o escribir el nombre.

-luego de seleccionar el archivo de entrada le pedira elegir el algoritmo mediante un menu desplegable (GUI) o de numeros (CMD),
una vez seleccionado el algoritmo correspondiente este mostrara la solucion por pantalla (consola) y tambien escribira la solucion
en un archivo txt dentro de la carpeta outputs

-cabe aclarar que mientras no selecione la opcion de cargar nueva entrada o salir puede correr todos los algoritmos con la mism
entrada cargada