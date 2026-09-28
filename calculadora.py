"""
Calculadora simple en Python
Proyecto Integrador - Git y GitHub
"""


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b


def mostrar_menu():
    print("\n===== Calculadora =====")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


def pedir_numero(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            return float(entrada)
        except ValueError:
            print("Entrada inválida. Por favor ingresá un número.")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elegi una opcion (1-5): ")

        if opcion == "5":
            print("Hasta luego!")
            break

        if opcion not in ("1", "2", "3", "4"):
            print("Opcion invalida, intenta de nuevo.")
            continue

        num1 = pedir_numero("Ingresá el primer número: ")
        num2 = pedir_numero("Ingresá el segundo número: ")

        if opcion == "1":
            print(f"Resultado: {sumar(num1, num2)}")
        elif opcion == "2":
            print(f"Resultado: {restar(num1, num2)}")
        elif opcion == "3":
            print(f"Resultado: {multiplicar(num1, num2)}")
        elif opcion == "4":
            try:
                print(f"Resultado: {dividir(num1, num2)}")
            except ValueError as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    main()