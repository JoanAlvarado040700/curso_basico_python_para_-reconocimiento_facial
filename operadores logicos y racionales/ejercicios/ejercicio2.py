#ejercicio2 

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))


print(f"El valor de a es: {a} y el de b es {b} ")

a = int(input("Ingrese el nuevo valor de a: "))
b = int(input("Ingrese el nuevo valor de b: "))

print(f"Los nuevos valores para a: {a} y b es: {b} ")

print("Ahora se intercambian los valores")

a,b =b,a
print(f"A: {a} ")
print(f"B: {b} ")