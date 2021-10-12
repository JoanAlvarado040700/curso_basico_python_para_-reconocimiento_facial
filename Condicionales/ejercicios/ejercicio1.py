# Ingresar dos valores y mostrar por pantalla cual es el par o impar

dato1 = int(input("Ingrese el primer valor  \n ") )
dato2 = int(input("Ingrese el segundo valor ") )

if (dato1 %2 == 0 and dato2 %2 != 0 ):
    print(f"El primer valor: {dato1} es par \n el valor: {dato2} es inpar ")
elif (dato2 %2 == 0 and dato1 %2 != 0 ):
    print(f"El primer valor: {dato2} es par \n el valor: {dato1} es inpar ")
elif (dato2 %2 != 0 and dato1 %2 != 0 ):
    print("Ambos valores son inpares ")
else:
    print("Ambos numeros son pares")

