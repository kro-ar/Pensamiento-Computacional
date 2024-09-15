#S2: Sentencias Basicas
#Flujo de Control de un Programa (FCP)
#Una secuencia de sentencias ordenadas renglon por renglon y respentando su sintaxis
#Funciones:
#Es codigo reutilizable que realiza una tarea especifica.

#Disponemos de una amplia gama de funciones predefinidas tales como:
#print(),input(), abs(), round(),
#int(), float(), str(), bool(), len()

#Para definir funciones propias utilizamos el comando 'def'

def saludar(nombre): #definir funcion
    print(f"Hola, {nombre}")

saludar("Caro") #Llama a la función y muestra "Hola, 'nombre'"

#Diferencia entre RETURN y PRINT
#return devuelve un valor y termina la ejecucion de la funcion
#print solo muestra el valor y no devuelve nada


#Variables
#Es el nombre que se asocia a un valor variable
#a lo largo de la ejecucion del programa
#edad = 25 variable que almacena un numero
#se escriben en uppercase


#Constantes 
#Es un valor no variable durante la ejecucion
#PI = 3.1416 normalmente se escribe en mayusculas

#Tipos de Datos
# entero - int = 9
#real - float = 0.01
#complejo - complex =1+2j
#logico - bool = True / False
#texto - str = "Hola"

#Texto,String o Cadena (str) referencia la secuencia de caracteres sean letras,numeros
# o simbolos
#Se usa para almacenar y manipular texto
#Cadenas de caracteres ordenados cuya posicion
#inicia en 0,de izquierda a derecha

palabra="pensamiento"
print(palabra[2])

#Rangos
#Start desde donde inicia la cadena (0)
#End hasta donde se define que llegue excluyendo la posicion ([5] llega a 4ta posicion)
#Setp cada cuanto se va aumentando la posicion(1)

#[start:end:step]
print(palabra[1:6:2])

#Si un valor no es asignado se queda el valor predeterminado
#Start 0
#End -1
#Step 1
print(palabra[:6:2])
print(palabra[1::2])
print(palabra[1:6:])

#Input 
#Es una funcion que permite obtener la entrada de un user

materia=input('Complete el nombre de la materia: ')
print(palabra+ " " + materia )

