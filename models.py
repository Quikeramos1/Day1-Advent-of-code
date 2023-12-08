#Funciones

dnums = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
         "six": 6, "seven": 7, "eight": 8, "nine": 9}

def abrir(file):

    try:
        open_file = open(file, "r")
        return open_file

    except FileNotFoundError:
        print("El archivo indicado no existe\no no se ha podido abrir")
        exit()


def calcular(open_file):

    lista_final = []
    contador = 0

    for linea in open_file:
        contador += 1
        linea = linea.rstrip()
        lista_linea = []
        lista_text = []
    


        for i in linea:
            lista_text.append(i)

            try:
                i = int(i)
                lista_linea.append(i)

            except:
                text_final = "".join(lista_text).lower()
                for num in dnums:
                    if num in text_final:
                        num = dnums[num]
                        lista_linea.append(num)
                        lista_prov = lista_text[-2],lista_text[-1]
                        lista_text = list(lista_prov)
                        
                        break

        digitos = str(lista_linea[0]) + str(lista_linea[-1])
        digitos = int(digitos)
        lista_final.append(digitos)

    resultado = sum(lista_final)
    return resultado, contador, lista_final