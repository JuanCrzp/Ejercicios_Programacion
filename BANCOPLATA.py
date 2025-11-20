
class CuentaBancaria:
    def __init__(self):
        self.__nombre = "ariel"
        self.__saldo = 10_000_000 

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        if nuevo_nombre != "":
            self.__nombre = nuevo_nombre
        else:
            print("el nombre no puede estar vacío")

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def depositar(self, cantidad):  
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito aceptado de {cantidad:,.0f}. Nuevo saldo: {self.__saldo:,.0f}")
        else:
            print("Solo se aceptan depósitos positivos")

    def retirar(self, cantidad):
        if cantidad < 20_000:
            print("El valor mínimo para retirar es de 20.000")
        elif cantidad > self.__saldo:
            print("Saldo insuficiente")
        else:
            self.__saldo -= cantidad
            print(f"Retiro aceptado valor de {cantidad:,.0f}. Nuevo saldo: {self.__saldo:,.0f}")

cuenta = CuentaBancaria()
print(f"Bienvenido {cuenta.get_nombre()}")
print(f"El saldo de su cuenta es de: {cuenta.get_saldo():,.0f}")

while True: 
    print(" ============== Menu Cuenta BANCOPLATA ===============")
    print("1. retirar plata")
    print("2. depositar plata")
    print("3. consultar mi saldo")
    print("4. cambiar nombre del titular")
    print("5. salir")

    opcion = input("Elija una opción (1-5): ")

    if opcion == "1":
        print("opciones de retiro:")
        print("1. 20.000")
        print("2. 50.000")
        print("3. 100.000")
        print("4. especificar algun valor")
        opcion_retiro = input("Elija una opción: ")

        if opcion_retiro == "1":
            cuenta.retirar(20_000)
        elif opcion_retiro == "2":
            cuenta.retirar(50_000)
        elif opcion_retiro == "3":
            cuenta.retirar(100_000)
        elif opcion_retiro == "4":
            valor_raw = input("Ingrese el valor que desea retirar: ")
            try:
                valor = float(valor_raw.replace(".", "").replace(",", ""))
                cuenta.retirar(valor)
            except ValueError:
                print("Debes ingresar un número válido.")
        else:
            print("Opción no válida")

    elif opcion == "2":
        valor_raw = input("Ingrese el valor que desea depositar: ")
        try:
            valor = float(valor_raw.replace(".", "").replace(",", ""))
            cuenta.depositar(valor)
        except ValueError:
            print("Debes ingresar un número válido.")

    elif opcion == "3":
        print(f"Cliente: {cuenta.get_nombre()}")
        print(f"Saldo actual: {cuenta.get_saldo():,.0f}")

    elif opcion == "4":
        nuevo = input("Ingrese el nuevo nombre del titular: ")
        cuenta.set_nombre(nuevo)

    elif opcion == "5":
        print(f"Gracias por usar nuestro sistema bancario Bancoplata, {cuenta.get_nombre()}.")
        break

    else:
        print("Opción no válida, intenta nuevamente")