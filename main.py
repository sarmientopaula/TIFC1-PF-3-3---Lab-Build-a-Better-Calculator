def main():
  print("Hello learners!")

# Función que suma una lista de números
def addmultiplenumbers(numbers):
    return sum(numbers)

# Función que multiplica una lista de números consecutivamente
def multiplymultiplenumbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Función que verifica si un número es entero y par
def isiteven(num):
    # Primero verifico si es entero
    if isinstance(num, int):
        return num % 2 == 0
    else:
        return False

# Función que verifica si un valor es un entero
def isitaninteger(num):
    return isinstance(num, int)

# Función principal con la lógica interactiva
def main():
    print("Hello learners!")
    print("Bienvenidos a mi calculadora mejorada :D")

    # Ejemplo interactivo (opcional para pruebas manuales)
    opcion = input("¿Qué deseas probar? (sumar/multiplicar/par/entero/salir): ").lower()

    if opcion == "sumar":
        nums = input("Ingresa números separados por espacios: ")
        lista = [float(n) for n in nums.split()]
        print("Resultado:", addmultiplenumbers(lista))

    elif opcion == "multiplicar":
        nums = input("Ingresa números separados por espacios: ")
        lista = [float(n) for n in nums.split()]
        print("Resultado:", multiplymultiplenumbers(lista))

    elif opcion == "par":
        num = float(input("Ingresa un número: "))
        print("¿Es par?:", isiteven(num))

    elif opcion == "entero":
        num = float(input("Ingresa un número: "))
        print("¿Es entero?:", isitaninteger(num))

    else:
        print("Saliendo...")


if __name__=="__main__":
  main()