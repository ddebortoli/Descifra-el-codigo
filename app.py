from flask import Flask,request,jsonify,render_template
from formula import subsetSum
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/')
def init():
    return render_template('index.html')

@app.route('/posibilidades', methods=['POST'])
def index():
    numerosPosibles = [
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
    
    misNumeros = request.json['misNumeros']    
    misNumeros = [misNumeros['A'],misNumeros['B'],misNumeros['C'],misNumeros['D'],misNumeros['E']] or None
    
    sumaNegras = request.json['Suma negros']
    sumaBlancas = request.json['Suma blancos']
    sumatoriaTotal = request.json['Suma total']
    cantidadNegras = request.json['Cantidad negras']
    cantidadBlancas = request.json['Cantidad blancas']
    
    # Quitamos nuestros numeros de los valores posibles
    for numero in misNumeros:
        numerosPosibles.remove({int(numero['valor']):numero['color']})
    
    sumaBlancas = sumPorColor(misNumeros,sumaBlancas,'BLANCO',cantidadBlancas) if (sumaBlancas or cantidadBlancas) else []
    sumaNegras = sumPorColor(misNumeros,sumaNegras,'NEGRO',cantidadNegras) if (sumaNegras or cantidadNegras) else []
    sumaTotales = sumPorCantDigitos(numerosPosibles,sumatoriaTotal,5) if (sumatoriaTotal) else []
    
    return jsonify({"suma Negros":sumaNegras,"suma Blancos": sumaBlancas,"suma Total":sumaTotales})

def sumPorColor(misNumeros,resultado,color,cantidad = 5):
    blancas = [{0: 'BLANCO'},   
    {1: 'BLANCO'},
    {2:"BLANCO"},
    {3:"BLANCO"},
    {4:"BLANCO"},
    {6:"BLANCO"},
    {7:"BLANCO"},
    {8:"BLANCO"},
    {9:"BLANCO"}]
    negras = [{0: 'NEGRO'},   
    {1: 'NEGRO'},
    {2:"NEGRO"},
    {3:"NEGRO"},
    {4:"NEGRO"},
    {6:"NEGRO"},
    {7:"NEGRO"},
    {8:"NEGRO"},
    {9:"NEGRO"}]
    
    if color == 'NEGRO':
        lista = negras
    else:
        lista = blancas
            
    
    for numero in misNumeros:
        if numero['color'] == color:
            lista.remove({int(numero['valor']):numero['color']})                
    return subsetSum(lista,resultado,cantidad)

def sumPorCantDigitos(numeros,resultado,cantidad):              
    return subsetSum(numeros,resultado,cantidad)


app.run(host='0.0.0.0', port=81,debug=True)