from flask import Flask, jsonify
import json
import os

app3 = Flask(__name__)

MUNICIPIO_JSON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "municipio.json"))
DEMO_JSON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "demo.json"))

@app3.route('/<int:municipioid>/demo', methods=['GET'])
def get_demo(municipioid):
    try:
        # Validar que el ID sea 23006
        if municipioid != 23006:
            return jsonify({"error": "Municipio no encontrado"}), 404

        # Cargar datos de municipio.json
        with open(MUNICIPIO_JSON_PATH, 'r', encoding='utf-8') as f:
            municipios = json.load(f)

        # Cargar datos de demo.json
        with open(DEMO_JSON_PATH, 'r', encoding='utf-8') as f:
            demos = json.load(f)

        # Devolver ambos JSON
        result = {
            "municipios": municipios,
            "demo": demos
        }

        return jsonify(result), 200

    except FileNotFoundError:
        return jsonify({"error": "Archivo JSON no encontrado"}), 500
    except json.JSONDecodeError:
        return jsonify({"error": "Error al leer los JSON"}), 500

if __name__ == '__main__':
    app3.run(port=5002)

