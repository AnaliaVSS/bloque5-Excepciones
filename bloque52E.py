def simple_math_operations(values):
    try:
        total_sum = sum(values)
        average = total_sum / len(values)
        division = values[0] / values[-1]
        return total_sum, average, division
    except ZeroDivisionError:
        return "Error: División por cero."
    except TypeError:
        return "Error: Tipo de dato inválido."

# Ejemplo de uso
values_list = [10, 20, 30, 40]
result = simple_math_operations(values_list)
print(result)
