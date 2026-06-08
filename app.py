from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# La API KEY la configuraremos en el servidor, no aquí
API_KEY = os.getenv("GEMINI_API_KEY")
CODIGO_DUENO = "33489679"

@app.route('/jarvis', methods=['POST'])
def jarvis():
    data = request.json
    if data.get("codigo") != CODIGO_DUENO:
        return jsonify({"error": "Acceso denegado"}), 403
    
    mensaje = data.get("mensaje")
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
    headers = {"x-goog-api-key": API_KEY, "Content-Type": "application/json"}
    
    response = requests.post(url, headers=headers, json={"contents": [{"parts": [{"text": mensaje}]}]})
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
  
