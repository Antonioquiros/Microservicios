from flask import Flask, jsonify
import json

app3 = Flask(__name__)
@app3.route('/<int:municipioid>/demo', methods=['GET'])
def get_demo(municipioid):


# Función

if __name__ == '__main__':
    app3.run(port=5002)
    