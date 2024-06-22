import statistics as st

try:
    with open('datos.txt', 'r') as datos:
        numeros = datos.read().splitlines()
        intConvertor = [int (i) for i in numeros]   #Convertidor de string a integer
        numeros = intConvertor
