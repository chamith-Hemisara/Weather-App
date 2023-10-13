from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your OpenWeatherMap API key
API_KEY = "1e87c0f89446f663de746d6125811adf"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    location = request.form['location']

    if not location:
        return render_template('index.html', error='Please enter a location.')

    try:
        # Fetch current weather data
        current_response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}")
        current_data = current_response.json()
        current_temperature = current_data['main']['temp'] - 273.15  # Convert temperature from Kelvin to Celsius

        # Fetch weather forecast data
        forecast_response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}")
        forecast_data = forecast_response.json()

        return render_template('index.html', location=location, current_temperature=current_temperature, forecast=forecast_data['list'])
    except:
        return render_template('index.html', error='Location not found.')

if __name__ == '__main__':
    app.run(debug=True)
