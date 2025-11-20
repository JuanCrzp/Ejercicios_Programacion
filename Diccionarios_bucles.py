# ==============================
# Taller: Diccionarios y Bucles
# ==============================

# 1. Diccionario con minimo 3 pares clave-valor
agenda = {
"nombre": "Cita medica",
"dia": "20 noviembre",
"lugar": "Hospital central"
}
print("Diccionario inicial:")
print(agenda)
print("-" * 50)

# 2. Adicionar un elemento al diccionario
agenda["direccion"] = "calle 65 b 40-30"
print("Diccionario despues de adicionar un elemento:")
print(agenda)
print("-" * 50)

# 3. Eliminar un elemento del diccionario
del agenda["dia"]
print("Diccionario despues de eliminar un elemento:")
print(agenda)
print("-" * 50)

# 4. Input solicitando informacion al usuario
numeros_usuarios = int(input("Cuantos usuarios desea evaluar?: "))
print("Numero de usuarios ingresado:", numeros_usuarios)

usuarios2 = int(input("Ingrese el usuario numero 2: "))
print("Usuario 2 ingresado:", usuarios2)
print("-" * 50)

# 5. Bucles for

print("Bucle for con inicio y fin (1 al 9):")
for varnumero in range(1, 10):
	print(varnumero)
print("Termina el proceso")
print("-" * 50)


print("Bucle for con paso (de 2 en 2, del 1 al 9):")
for var2 in range(1, 10, 2):
	print(var2)
print("Termina el proceso")
print("-" * 50)


print("Bucle for con un solo argumento (0 al 14):")
for var2 in range(15):
	print(var2)
print("Termina el proceso")
print("-" * 50)


print("Bucle for con inicio, fin y paso (de 5 en 5, del 5 al 15):")
for var in range(5, 20, 5):
	print(var)
print("Termina el proceso")
print("-" * 50)

# Bucle while

print("Bucle while:")
contador = 0
while contador < 5:
	print(contador)
	contador += 1
	print(f"Valor variable contador: {contador}")
print("Fin del programa")