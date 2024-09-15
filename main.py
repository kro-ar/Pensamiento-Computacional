#S2: Sentencias Basicas - Ejercicios
#Intentá ser lo más amigable posible con el usuario!

#Ejercicio 1
#Crear un programa que le solicite al usuario un entero y lo imprima por pantalla.

numero = input('Ingrese un numero del 1 al 4:')
print ('Eligio el numero:' + numero)

#Ejercicio 2
#Crear un programa que le solicite al usuario dos números enteros y luego imprima por pantalla:

num1 = int(input('Ingrese un numero:'))
num2 = int(input('Ingrese otro numero:'))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
resultado = suma,resta,multiplicacion,division
print(resultado)

#Ejercicio 3
#Crear un programa que le solicite al usuario un entero y determine si es par
#Mostrando por pantalla un mensaje que indique el resultado

numero = int(input("Ingresa un número entero: "))
resultado = "par" if numero % 2 == 0 else "impar"
print(f"El número {numero} es {resultado}.")

#Ejecicio 4
#Escribir un programa que le pida a un usuario su año de nacimiento y otro año
#Y le diga qué edad tenía el usuario en el año ingresado.

anioNac = int(input("Ingrese su año de nacimiento:"))
anioExt = int(input("Ingrese otro año:"))
edad = anioExt - anioNac
print("En el año", anioExt , "tenia la edad de ", edad)

#Ejercio 5
#Crear un programa que le solicite al usuario 5 enteros
#Y muestre por pantalla el promedio de ellos

nums1 = int(input("Ingrese un numeros entero:"))
nums2 = int(input("Ingrese un numeros entero:"))
nums3 = int(input("Ingrese un numeros entero:"))
nums4 = int(input("Ingrese un numeros entero:"))
nums5 = int(input("Ingrese un numeros entero:"))
resultado = (nums1 + nums2 + nums3 + nums4 + nums5) / 5
print(resultado)

#Ejercio 6
#Crear una función que reciba un número 
#Y muestre el anterior y el siguiente.

numIng = input("Ingrese un numero:")
numAnt = int(numIng)-1
numSig = int(numIng)+1
print("El numero ingresado es", numIng, "el numero anterior es", numAnt , "y el numero siguiente es ", numSig)

#Ejercio 7
#Crear una función que una un string y un entero, ambos dentro de un string

nombre = input("Ingrese su nombre:")
edad = int(input("Ingrese su edad:"))
print(f"Hola", {nombre},"tienes",{edad})

#Ejercio 8 
#Pedirle nombre y apellido por separado e imprimir “Apellido, Nombre”

nomb = input("Ingrese su nombre:")
apell = input("Ingrese su apellido:")
print("Su nombre completo es:", nomb ,"", apell)

#Ejecicio 9 
#Obtener una palabra e imprimir la cantidad de letras
palabra = input("Ingrese una palabra:")
cantPal = len(palabra)
print("Su palabra contiene",cantPal, "caracteres")

#Ejercicio 10
#Obtener una palabra e imprimir los primeros 5 caracteres

palabra = input("Ingrese una palabra:")
print(palabra[:5:])

#Ejercicio 11
#Obtener una palabra, borrarle todas las ‘a’ e imprimirla por pantalla
palabra = input("Ingrese una palabra que contenga la letra a:")
palabra_sin_a = palabra.replace('a', '').replace('A', '')
print(palabra_sin_a)