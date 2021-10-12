#ejercicio 4: 

'''
Obtener el precio final que se tiene que pagar 
si se aplica el 36% de descuento total de la compra 

'''


producto1 = int(input("Ingrese el valor del producto 1: "))
producto2 = int(input("Ingrese el valor del producto 2: "))
producto3 = int(input("Ingrese el valor del producto 3: "))
#Este es el descuento en porcentaje que se pedia 
descuento= 36/100 #Tambien se puede describir como 0.36

total = (producto1+producto2+producto3)*descuento
nt =producto1+producto2+producto3
ahorro = nt - total
print(f"El total a pagar es de: {total} ")
print(f"El neto a pagar era: {nt} ")
print(f"Con el descuento ahora: {ahorro} ")
