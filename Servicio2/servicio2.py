from flask import Flask, jsonify
import requests

app2 = Flask(__name__)

@app2.route('/<int:municipioid>/meteo', methods=['GET'])
def get_meteo(municipioid):
    url = f"https://www.el-tiempo.net/api/json/v2/provincias/23/municipios/{municipioid}"
    response = requests.get(url)
    
    if municipioid != 23006:
        return "Este municipio no es Arjona", 404
    
    if response.status_code != 200:
        return jsonify({"error": "Municipio no encontrado"}), 404
    
    data = response.json()
    
    if 'municipio' not in data or 'prediccion' not in data:
        return jsonify({"error": "Datos meteorológicos no disponibles"}), 500
    
    meteo_info = {
        "temperatura": data.get("temperatura_actual", "N/A"),
        "temperatura_max": data.get("prediccion", {}).get("dia", [{}])[0].get("temperatura", {}).get("maxima", "N/A"),
        "temperatura_min": data.get("prediccion", {}).get("dia", [{}])[0].get("temperatura", {}).get("minima", "N/A"),
        "humedad": data.get("humedad", "N/A"),
        "viento": data.get("prediccion", {}).get("dia", [{}])[0].get("viento", {}).get("velocidad", "N/A"),
        "precipitacion": data.get("prediccion", {}).get("dia", [{}])[0].get("precipitacion", "N/A"),
        "lluvia": data.get("prediccion", {}).get("dia", [{}])[0].get("estado_cielo", "N/A")
    }
    
    return jsonify(meteo_info), 200

@app2.route('/')
def home():
    return "Microservicio 2 en funcionamiento", 200

if __name__ == '__main__':
    app2.run(port=5001, debug=True)