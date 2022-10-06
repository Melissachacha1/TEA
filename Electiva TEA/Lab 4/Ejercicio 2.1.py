contador = 0
suma= 0
minimo = 0
maximo= 0
primernumero=0
while True:
    try:
        numero= input("Ingrese un número: ")
        if (numero == "salir"):
            break
        else:
            contador = contador + 1
            suma= suma + int(numero)
            if(primernumero):
                minimo= int(numero)
                maximo= minimo
                primernumero= False
            else:
                if(int(numero)> maximo):
                    maximo = int(numero)
                if (int(numero)< minimo):
                    minimo = int(numero)
    except:
        print("Debe ingresar un valor numérico")
        contador = contador - 1
print("Contadir: ", contador)
print ("Suma: ", suma)
print ("Máximo: ", maximo)
print ("Mínimo: ", minimo)
