def suma (a, b):
    return a + b

def resta (a, b):
    return a - b
def multiplicacion (a, b):
    return a * b    
def division (a, b):
    return a/b

def potencia (a, b):
    return a**b



CalcActiva = True

if CalcActiva == True:
    print("***********************\nCalculadora\n***********************")
    opcion = input("Elija una opción\n1. Sumar\n2.Restar\n3.Multiplicar\n4.Dividir\n5.Salir\n")
    if opcion == "5":
        CalcActiva = False
        print("...Apagando calculadora...")
    elif opcion == "1":
        print("Suma de dos números")
        n1 = int(input("Primer número: "))
        n2 = int(input("Segundo número: "))
        resultado = suma(n1,n2)
        print (resultado)
