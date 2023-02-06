import math

def jugar(intento=1): 
    respuesta = input("¿De qué color es una naranja? ") 
    if respuesta != "naranja": 
        if intento < 3: 
            print ("\nFallaste! Inténtalo de nuevo") 
            intento += 1 
            jugar(intento) # Llamada recursiva 
        else: 
            print( "\nPerdiste!" )
    else:
        print ("\nGanaste!") 

def imprimir_doble(x):
    print(x,x,sep=" - ")

def digitos(x):
    lista = list(set(str(x)))
    lista = [int(x) for x in lista]
    return(sorted(lista))

def distancia(x,y):
    pit = math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)
    man = abs(x[0]-y[0]) + abs(x[1]-y[1])
    dic = {'manhattan':man, 'pitagoras':pit}
    return(dic)

def mediana(x):
    return(x[len(x)//2])