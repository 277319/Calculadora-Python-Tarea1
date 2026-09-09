def suma (a, b):
    return a + b

def resta (a, b):
    return a - b

def multiplicacion (a, b):
    return a * b    

def division (a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b

def potencia(a: float, b: float) -> float:
    """Calcula la potencia de la base a elevada al exponente b."""
    return a ** b

def desea_continuar():
    """Pregunta al usuario si desea hacer otra operación o salir."""
    while True:
        respuesta = input("\n¿Desea realizar otra operación? (s/n): ").strip().lower()
        if respuesta in ["s", "si", "sí"]:
            return True
        elif respuesta in ["n", "no"]:
            return False
        else:
            print("Opción no válida. Ingrese 's' para continuar o 'n' para salir.")

def raiz_cuadrada(a: float) -> float:
    if a < 0:
        print ("Error: No se puede calcular con número negativo")
        return "Error"
    return a ** 0.5

CalcActiva = True

while CalcActiva:
    print("***********************\nCalculadora\n***********************")
    opcion = input("Elija una opción\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Potencia\n6. Raíz Cuadrada\n7. Salir\n")
    
    if opcion == "7":
        CalcActiva = False
        print("...Apagando calculadora...")

    elif opcion == "1":
        print("Suma de dos números")
        n1 = int(input("Primer número: "))
        n2 = int(input("Segundo número: "))
        resultado = suma(n1, n2)
        print("Resultado:", resultado)

    elif opcion == "2":
        print("Resta de dos números")
        n1 = int(input("Primer número: "))
        n2 = int(input("Segundo número: "))
        resultado = resta(n1, n2)
        print("Resultado:", resultado)

    elif opcion == "3":
        print("Multiplicación de dos números")
        n1 = int(input("Primer número: "))
        n2 = int(input("Segundo número: "))
        resultado = multiplicacion(n1, n2)
        print("Resultado:", resultado)

    elif opcion == "4":
        print("División de dos números")
        n1 = int(input("Primer número: "))
        n2 = int(input("Segundo número: "))
        resultado = division(n1, n2)
        print("Resultado:", resultado)

    elif opcion == "5":
        print("Potencia de un número")
        n1 = int(input("Base: "))
        n2 = int(input("Exponente: "))
        resultado = potencia(n1, n2)
        print("Resultado:", resultado)

    elif opcion == "6":
        print("Raíz cuadrada de un número")
        n1 = float(input("Número: "))
        resultado = raiz_cuadrada(n1)
        print("Resultado:", resultado)

    else:
        print("Opción no válida. Intente nuevamente.\n")

    # Si eligió una operación matemática válida, preguntamos si desea seguir
    if opcion in ["1", "2", "3", "4", "5", "6"]:
        if not desea_continuar():
            CalcActiva = False
            print("...Apagando calculadora...")