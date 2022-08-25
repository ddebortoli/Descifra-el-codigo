from itertools import combinations
  
##Posibilidades
## Suma sin saber cantidad de numeros
## Suma sabiendo cantidad de numeros
def subsetSum(numerosPosibles, SumaTotal,cantNumeros = None):
    resultados = []
    tenemosCantidadNumeros = True
    # Iterating through all possible
    # subsets of arr from lengths 0 to n:
    if(cantNumeros == None):
        cantNumeros = 5
        tenemosCantidadNumeros = False
    
    SumaTotal = convertToInt(SumaTotal)
    cantNumeros = convertToInt(cantNumeros)
    
    for i in range(1,(cantNumeros + 1)):
        for subset in combinations(numerosPosibles, i):
            if(tenemosCantidadNumeros):
                if(SumaTotal):
                    if len(subset) == (cantNumeros) and returnSum(subset) == SumaTotal:
                        resultados.append(subset)  
                elif len(subset) == (cantNumeros):
                    resultados.append(subset)
            else:
                if SumaTotal:
                    if returnSum(subset) == SumaTotal:
                        resultados.append(subset)
                else:
                    resultados.append(subset)
    return resultados

def convertToInt(number):
    try:
        return int(number)
    except:
        return None

def returnSum(subset):
    "Devuelve la suma de las claves del subset"
    res = [ele for key in subset for ele in key]
    return sum(res)

