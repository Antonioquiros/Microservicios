from flask import Flask, jsonify
import json

app1 = Flask(__name__)

@app1.route('/<int:municipioid>/geo', methods=['GET'])
def get_geo(municipioid):
    url = f"https://www.el-tiempo.net/api/json/v2/provincias/23/municipios/{municipioid}"
    response = json.get(url)

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({"error": "Municipio no encontrado"}), 404

@app1.route('/')
def home():
    return "Microservicio 1 en funcionamiento", 200

if __name__ == '__main__':
    app1.run(port=5000)