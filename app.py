from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    api_key = "a916efd49322bc59968ba36bc2c3e587"
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'City not found'}), 404

if __name__ == "__main__":
    app.run(debug=True)
