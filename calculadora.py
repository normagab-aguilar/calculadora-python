"""
Calculadora simple en Python
Proyecto Integrador - Git y GitHub
"""


def sumar(a, b):
    return a + b


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
        opcion = input("Elegí una opción (1-5): ")

        if opcion == "5":
            print("¡Hasta luego!")
            break

        if opcion == "1":
            num1 = pedir_numero("Ingresá el primer número: ")
            num2 = pedir_numero("Ingresá el segundo número: ")
            print(f"Resultado: {sumar(num1, num2)}")
        else:
            print("Función aún no implementada.")


if __name__ == "__main__":
    main()