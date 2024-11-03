from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Sample API endpoints for country info, weather, currency rates, etc.

# Endpoint to get country data
@app.route('/api/countries', methods=['GET'])
def get_countries():
    try:
        # Fetch country data from REST Countries API
        response = requests.get('https://restcountries.com/v3.1/all')
        countries = response.json()
        return jsonify(countries), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get weather for a specific city
@app.route('/api/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    api_key = "YOUR_OPENWEATHER_API_KEY"  # Replace with your OpenWeather API key
    try:
        weather_response = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        )
        weather_data = weather_response.json()
        return jsonify(weather_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get currency exchange rates
@app.route('/api/currency', methods=['GET'])
def get_currency_rate():
    base_currency = request.args.get('base')
    target_currency = request.args.get('target')
    api_key = "YOUR_EXCHANGERATE_API_KEY"  # Replace with your ExchangeRate API key
    try:
        currency_response = requests.get(
            f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}'
        )
        currency_data = currency_response.json()
        return jsonify(currency_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
