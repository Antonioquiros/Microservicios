from flask import Flask, jsonify
import requests

app4 = Flask(__name__)

# Definir las URLs de los otros servicios
SERVICES = {
    "geo": "http://localhost:5000/{municipioid}/geo",
    "meteo": "http://localhost:5001/{municipioid}/meteo",
    "demo": "http://localhost:5002/{municipioid}/demo"
}

@app4.route('/<int:municipioid>/<param1>/<param2>', methods=['GET'])
def get_combined(municipioid, param1, param2):
    params = {param1, param2}  # Convertir en conjunto para manejar cualquier orden
    response_data = {}

    # Verificar qué servicios solicitar
    for param in params:
        if param in SERVICES:
            url = SERVICES[param].format(municipioid=municipioid)
            response = requests.get(url)
            if response.status_code == 200:
                response_data[param] = response.json()
            else:
                response_data[param] = {"error": f"No se pudo obtener datos de {param}"}
        else:
            response_data[param] = {"error": "Parámetro no válido"}

    return jsonify(response_data), 200

if __name__ == '__main__':
    app4.run(port=5003)