from flask import Flask, jsonify
import json
import os

app3 = Flask(__name__)

MUNICIPIO_JSON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../municipio.json"))
DEMO_JSON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../demo.json"))

@app3.route('/<int:municipioid>/demo', methods=['GET'])
def get_demo(municipioid):
    try:
        # Cargar datos de municipio.json
        with open(MUNICIPIO_JSON_PATH, 'r', encoding='utf-8') as f:
            municipios = json.load(f)

        # Buscar el municipio por ID
        municipio = next((m for m in municipios if m["municipioid"] == municipioid), None)

        # Cargar datos de demo.json
        with open(DEMO_JSON_PATH, 'r', encoding='utf-8') as f:
            demos = json.load(f)

        # Buscar la información en demo.json comparando "Codigo geografico" con municipioid
        demo_data = next((d for d in demos if d["Codigo geografico"] == municipioid), None)

        if municipio and demo_data:
            # Fusionar ambas informaciones en un solo diccionario
            result = {**municipio, **demo_data}
            return jsonify(result), 200
        else:
            return jsonify({"error": "Datos no encontrados para el municipio"}), 404

    except FileNotFoundError:
        return jsonify({"error": "Archivo JSON no encontrado"}), 500
    except json.JSONDecodeError:
        return jsonify({"error": "Error al leer los JSON"}), 500

if __name__ == '__main__':
    app3.run(port=5002)
