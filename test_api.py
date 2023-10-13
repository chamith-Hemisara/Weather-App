import requests

# Replace with your OpenWeatherMap API key
API_KEY = "1e87c0f89446f663de746d6125811adf"
# Replace with a city or location you want to check
CITY = "Paris"

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("API key is working correctly!")
    print("Weather in", CITY)
    print("Temperature:", data['main']['temp'] - 273.15, "°C")
else:
    print("Error:", response.status_code)


