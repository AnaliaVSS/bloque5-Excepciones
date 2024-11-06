def calcular_factorial(n):
    try:
        # Verificar si el número es entero y positivo
        if not isinstance(n, int) or n < 0:
            raise ValueError("El número debe ser un entero positivo.")
        
        # Calcular el factorial
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        
        return factorial
    
    except ValueError as e:
        return f"Error: {str(e)}"
    except OverflowError:
        return "Error: El número es demasiado grande para ser procesado."

# Ejemplo de uso
numero = 5
resultado = calcular_factorial(numero)
print(resultado)
