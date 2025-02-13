from flask import Flask, jsonify
import requests

app2 = Flask(__name__)

@app2.route('/<int:municipioid>/meteo', methods=['GET'])
def get_meteo(municipioid):

if __name__ == '__main__':
    app2.run(port=5001)