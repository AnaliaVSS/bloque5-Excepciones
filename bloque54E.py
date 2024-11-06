# Definir la excepción personalizada
class NegativeNumberError(Exception):
    pass

def calcular_raiz_cuadrada(n):
    if n < 0:
        raise NegativeNumberError("No se puede calcular la raíz cuadrada de un número negativo.")
    return n ** 0.5

# Ejemplo de uso
try:
    numero = -4
    resultado = calcular_raiz_cuadrada(numero)
    print(resultado)
except NegativeNumberError as e:
    print(f"Error: {e}")
