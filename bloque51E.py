def main():
    try:
        num1 = int(input("Ingrese el primer número entero: "))
        num2 = int(input("Ingrese el segundo número entero: "))
        resultado = num1 / num2
        print(f"El resultado de dividir {num1} por {num2} es {resultado}")
    except ValueError:
        print("Error: Debe ingresar un número entero.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")

if __name__ == "__main__":
    main()
