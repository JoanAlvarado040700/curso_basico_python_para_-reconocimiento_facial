#Programa que pida 3 numeros y determine cual es el mayor 

dato1 = int(input("Ingrese un valor:") )
dato2 = int(input("Ingrese un valor:") )
dato3 = int(input("Ingrese un valor:") )

if(dato1 > dato2 or dato2 > dato3):
    print(f"El datos {dato1} es el mayor ")
elif dato2> dato1 and dato1 > dato3:
    print(f"El valor: {dato2} es mayor  ")
elif dato3 > dato1:
    print(f"El valor: {dato3} es el mayor ")
else:
    print("Los numeros son iguales")    
