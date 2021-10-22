#Cajero automatico
'''
Crear un programa que simule un cajero automatico 
con un saldo inicial de 2000 C$, con el siguente menu

1-> Ingreso de dinero
2-> Retiro de dinero
3-> Mostrar dinero
4->Salir
'''

user = input("Ingrese su usuario")
saldoIni = 2000

print(f"Bienvenido {user} al menu del cajero automatico")
print("Estas son las opciones:\n 1-> Ingresar dinero \n2->Retirar dinero \n 3-> Mostrar dinero \n 4->Salir  ")
opciones = int(input("Ingrese una opcion: "))
if(opciones == 1):
    dinero =int(input("Ingrese la cantidad: "))
    saldo = saldoIni + dinero
    print("Desaea conocer su saldo? \n Si \n No")
    consulta =input()
    if(consulta == "s"):
        print(f"Su saldo total es de: {saldo} ")
       
    else:
        exit
elif (opciones == 2):
    dinero =int(input("Ingrese la cantidad que desea retirar: "))
    saldo = saldoIni - dinero
    print("Desaea conocer su saldo? \n Si \n No")
    consulta =input()
    if(consulta == "s"):
        print(f"Su saldo total es de: {saldo} ")
    else:
        exit
elif (opciones == 3):
    print(f"Su saldo es de: {saldoIni} ")
elif (opciones == 4):
    exit
else:
    print("Opcion invalida")