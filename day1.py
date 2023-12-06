'''The newly-improved calibration document consists of lines of text;
each line originally contained a specific calibration value that the
Elves now need to recover. On each line, the calibration value can be 
found by combining the first digit and the last digit (in that order) 
to form a single two-digit number.'''

file = input("¿Qué archivo deseas abrir? ")

try:
    open_file = open(file)
except:
    print("El archivo indicado no existe\no no se ha podido abrir")
    exit()

lista_linea = []  
lista_final = []  
contador = 0
for linea in open_file:
    contador += 1
    linea = linea.rstrip()
    for i in linea:
        
        try: 
            int(i)
            lista_linea.append(i)
            digitos = 0    
            digitos = lista_linea[0]+lista_linea[-1]
            
            
            
        except:
            continue 
    
    digitos = int(digitos)
    lista_final.append(digitos)
    lista_linea = []
    resultado = sum(lista_final)


    
print(f"El documento contiene", contador, "lineas")
print(f"La cantidad de valores recopilados es de",len(lista_final))
print(f"La suma de todos los valores recopilados es",resultado)


