from models import *

file = input("¿Qué archivo deseas abrir? ")

open_file = abrir(file)

resultado, contador, lista_final = calcular(open_file)

print(f"El documento contiene", contador, "lineas")
print(f"La cantidad de valores recopilados es de", len(lista_final))
print(f"La suma de todos los valores recopilados es", resultado)
