import requests 

WEATHER_CODES = {
    0: "Clear sky",
    1: "Mostly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Freezing fog",
    51: "light drizzle",
    61: "light rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Light snow",
    73: "Moderate snow",
    75: "Heavy snow",
    77: "Snow grains",
    80: "Rain showers",
    85: "Light snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with light hail",
    99: "Thunderstorm wit heavy hail",
}

while True:
    city = input("Enter a city: ")
 

# Get latitude andl longitude data for the select city
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1" #Address we are going to use 
    geo_response = requests.get(geo_url) # We use this to request and receive data
    geo_data = geo_response.json() # This turns it into usable data. 

    # we are getting the cords from json for latitude and longitude

    try:
        latitude = geo_data["results"][0]["latitude"]
        longitude = geo_data["results"][0]["longitude"]
        break
    except KeyError:
        print("This is not a valid city. Try again.")
        

    # we are getting the weather data based on cords we pulled from json file earlier 
weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&temperature_unit=fahrenheit"
weather_response = requests.get(weather_url)    
weather_data = weather_response.json()


temperature = weather_data["current_weather"]["temperature"]

print(f"It's currently {temperature}°F in {city}.")
