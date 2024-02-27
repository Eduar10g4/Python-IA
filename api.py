from flask import Flask, request, jsonify
import json

app = Flask(__name__)
historial = []  # Lista para almacenar el historial

@app.route('/guardar_historial', methods=['POST', 'GET'])
def guardar_historial():
    if request.method == 'POST':
        data = request.json
        historial.append(data)  # Agregar los datos recibidos al historial
        return jsonify({"message": "Historial guardado exitosamente"})
    elif request.method == 'GET':
        # Ordenar los datos en el orden deseado
        historial_ordenado = []
        for item in historial:
            historial_ordenado.append({key: item[key] for key in sorted(item.keys())})
        
        # Generar la respuesta JSON sin los caracteres de escape
        respuesta_json = jsonify(historial_ordenado)
        respuesta_json.response[0] = respuesta_json.response[0].decode('unicode-escape')
        
        return respuesta_json

if __name__ == '__main__':
    app.run(debug=True)
