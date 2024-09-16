#S3 Estructuras de Control


#Valores numericos
#Aritmeticos + - * / // 
num1= 2
num2=3
resultado = num1 + num2

#Valores booleanos es decir TRUE o FALSE
#El conjunto de Operaciones se unifican con
#Operadores Logicos and or not 

#Que devuelven una EXPRESION en las que se usan
#Operadores Relacionales == != < > => 

numero_1 = 12
numero_2 = 45
numero_3 = 4
numero_4 = 76
numero_5 = 34

#exp1)
#(numero_1 > numero_3) True

#exp2
#(numero_2 == numero_1) False

#exp3
#(numero_2 < numero_4) and (numero_3 == numero_5) False

#exp4
#(numero_1 + numero_5 == numero_2) or (numero_3 >= numero_4) False

#Estructuras de Control Selectivas
 #if (si ) /elif (si sino ) / else (sino)
#Entonces se toma como :

lluvia = False
calor = True
if lluvia and calor :
 print("Llevar sombrilla y poca ropa")
elif lluvia and not calor:
  print ("Llevar sombrilla y abrigo")
elif calor and not lluvia:
  print ("No llevar sombrilla ni abrigo")
else:
  print ("No llevar sombrilla pero abrigarse")