def leer_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo, 'r')
        contenido = archivo.read()
        print(contenido)
    except FileNotFoundError:
        print("Error: El archivo no existe.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        try:
            archivo.close()
        except NameError:
            pass

# Ejemplo de uso
nombre_archivo = "ejemplo.txt"
leer_archivo(nombre_archivo)
