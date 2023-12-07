dnums = {"one":1, "two":2, "three":3, "four":4,"five":5,
             "six":6,"seven":7,"eight":8,"nine":9}

file = input("¿Qué archivo deseas abrir? ")

try:
    open_file = open(file)
    
except:
    print("El archivo indicado no existe\no no se ha podido abrir")
    exit()

lista_linea = [] 
lista_text = [] 
lista_final = []  
contador = 0

for linea in open_file:
    contador += 1
    linea = linea.rstrip()
    for i in linea:
                
        lista_text.append(i)

        try:
            i = int(i)
            lista_linea.append(i)

        except:
            text_final = "".join(lista_text)
            text_final.lower()
            for num in dnums:
                if num in text_final:
                    num = dnums[num]
                    lista_linea.append(num)
                    lista_text = []
                
            
         

    digitos = str(lista_linea[0])+str(lista_linea[-1])

        
        
            
              
                       
    
    
    digitos = int(digitos)
    lista_final.append(digitos)
    lista_linea = []
    lista_text = []
    resultado = sum(lista_final)


    
print(f"El documento contiene", contador, "lineas")
print(f"La cantidad de valores recopilados es de",len(lista_final))
print(f"La suma de todos los valores recopilados es",resultado)



