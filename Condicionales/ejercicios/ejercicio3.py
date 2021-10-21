'''
Crear un programa que compare dos nombres y verificar
si hay coinsidencia o no, si es que ambos nombres comienzan con la 
misma letra o termina con la misma letra.
'''

nombre1 = input("Ingrese un nombre: ")
nombre2 = input("ingrese el segundo nombre: ")

if(nombre1[0] == nombre2[0] or nombre1[-1] == nombre2[-1]):
    print("Si hay considencia")
else:
    print("No hay coinsidencia")
