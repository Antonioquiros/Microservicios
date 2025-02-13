from flask import Flask, jsonify
import json
import os

app1 = Flask(__name__)

# Ruta del archivo JSON
JSON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../municipio.json"))

@app1.route('/<int:municipioid>/geo', methods=['GET'])
def get_geo(municipioid):
    try:
        with open(JSON_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Buscar el municipio por ID
        municipio = next((m for m in data if m["municipioid"] == municipioid), None)

        if municipio:
            return jsonify(municipio), 200
        else:
            return jsonify({"error": "Municipio no encontrado"}), 404

    except FileNotFoundError:
        return jsonify({"error": "Archivo municipios.json no encontrado"}), 500
    except json.JSONDecodeError:
        return jsonify({"error": "Error al leer el JSON"}), 500

@app1.route('/')
def home():
    return "Microservicio 1 en funcionamiento", 200

if __name__ == '__main__':
    app1.run(port=5000)