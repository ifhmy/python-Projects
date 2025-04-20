import requests

# Your API key here
api_key = "2ae318dbf79e323de4c4730688c5ae1b"

# API URL
url = "https://api.weatherstack.com/current?access_key=" + api_key

# List of cities to get weather data for
supported_cities = ["London", "Singapore", "Shanghai"]

# Ask the user to choose a city
print("Supported Cities:")
for city in supported_cities:
    print(f"- {city}")

city_input = input("Enter the name of the city you want to get weather data for: ")

# Check if the entered city is in the supported cities list
if city_input in supported_cities:
    querystring = {"query": city_input}
    
    # Sending the GET request to the API
    response = requests.get(url, params=querystring)
    
    if response.status_code == 200:
        data = response.json()

        # Print the full response to understand the structure of the data
        print(f"Full Response for {city_input}:")
        print(data)  # Print the entire response to see the details

        # Check if the 'success' flag is True
        if data.get("success"):
            weather = data.get('current', {})
            print(f"City: {city_input}")
            print(f"Temperature: {weather.get('temperature', 'N/A')}°C")
            print(f"Weather Description: {', '.join(weather.get('weather_descriptions', []))}")
            print(f"Wind Speed: {weather.get('wind_speed', 'N/A')} km/h")
            print(f"Humidity: {weather.get('humidity', 'N/A')}%")
            print("-" * 40)
        else:
            print(f"Error with data for {city_input}: {data.get('error', {}).get('info', 'Unknown error')}")
    else:
        print(f"Failed to get data for {city_input}. Status code: {response.status_code}")
else:
    print(f"The city '{city_input}' is not supported. Please enter a valid city name from the supported list.")
