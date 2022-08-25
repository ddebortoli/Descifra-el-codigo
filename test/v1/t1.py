
def index():
    nums = [
    {0: 'NEGRO'}, {0: 'BLANCO'},   
    {1: 'NEGRO'}, {1: 'BLANCO'},
    {2:'NEGRO'},{2:"BLANCO"},
    {3:'NEGRO'},{3:"BLANCO"},
    {4:'NEGRO'},{4:"BLANCO"},
    {5:'VERDE'},{5:"VERDE"},
    {6:'NEGRO'},{6:"BLANCO"},
    {7:'NEGRO'},{7:"BLANCO"},
    {8:'NEGRO'},{8:"BLANCO"},
    {9:'NEGRO'},{9:"BLANCO"}]
    print(nums)
    num = {
        "A": {
            "valor": 0,
            "color": "BLANCO"
        },
        "B": {
            "valor": 6,
            "color": "NEGRO"
        },
        "C": {
            "valor": 1,
            "color": "BLANCO"
        },
        "D": {
            "valor": 1,
            "color": "NEGRO"
        },
        "E": {
            "valor": 2,
            "color": "BLANCO"
        }
    }
    
    misNums = [num['A'],num['B'],num['C'],num['D'],num['E']]
     
    for num in misNums:
        nums.remove({num['valor']:num['color']})
          
    print(nums)
    sumatoriaNegros = 10
    #sumatoriaBlancos = request.json['Suma blancos']
    #sumatoriaTotal = request.json['Suma total']
    cantidadNegros = 2
    #cantidadBlancas = request.json['Cantidad blancas']
    
    #todosLosNumeros = sorted(numerosNegros.key()+numerosBlancos)
    numerosNegros.extend(numerosBlancos)
    print(numerosNegros)
    #sumaNegros = sumPorColor(numerosNegros,misNums,sumatoriaNegros,'NEGRO',cantidadNegros)
    #sumaBlancos = sumPorColor(numerosBlancos,misNums,sumatoriaBlancos,'BLANCO',cantidadBlancas)
    #sumaTotales = sumPorCantDigitos(todosLosNumeros,misNums,sumatoriaTotal,5)
    

    #return jsonify({"suma Negros":sumaNegros,"suma Blancos": sumaBlancos, "suma Total": sumaTotales})

def sumPorColor(numeros,misNumeros,resultado,color,cantidad = 5):
    numeros.remove({5:"VERDE"}) #Removemos el 5 ya que es de color verde
    for num in misNumeros:
        if(num['color'] == color):
            numeros.remove({num['valor']:num['color']})           
    return subsetSum(numeros,(resultado),cantidad)

def sumPorCantDigitos(numeros,misNumeros,resultado,cantidad):
    for num in misNumeros:
        numeros.remove(int(num['valor']))
    return subsetSum(numeros,(resultado),cantidad)


index()