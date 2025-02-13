from flask import Flask, jsonify
import requests

app2 = Flask(__name__)

@app2.route('/<int:municipioid>/meteo', methods=['GET'])
def get_meteo(municipioid):
    url = f"https://www.el-tiempo.net/api/json/v2/provincias/23/municipios/{municipioid}"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "Municipio no encontrado"}), 404

    data = response.json()

    # Verificamos si los datos esperados existen en la respuesta
    if 'temperatura_actual' not in data or 'temperaturas' not in data:
        return jsonify({"error": "Datos meteorológicos no disponibles"}), 500

    # Extraemos los valores correctamente del JSON
    meteo_info = {
        "temperatura_actual": data.get("temperatura_actual", "N/A"),
        "temperatura_max": data.get("temperaturas", {}).get("max", "N/A"),
        "temperatura_min": data.get("temperaturas", {}).get("min", "N/A"),
        "humedad": data.get("humedad", "N/A"),
        "viento": data.get("viento", "N/A"),  # Directamente un número
        "precipitacion": data.get("precipitacion", "N/A"),
        "estado_cielo": data.get("stateSky", {}).get("description", "N/A")  # Corrige "lluvia"
    }

    return jsonify(meteo_info), 200

if __name__ == '__main__':
    app2.run(port=5001)