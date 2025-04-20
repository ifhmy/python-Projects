import requests


# API Key
api_key = '9a8ccd8134c8957cab64d35a9ffd57d1'
city_name = input("Enter city name: ")


# our website contain wether data
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric"

#  send Request to the API
response = requests.get(url)

# validate the response
if response.status_code == 200:
    print("Weather data retrieved successfully.")

    
    data = response.json()    
    for x in data['list']:
        temp = x['main']['temp']  # temp
        humidity = x['main']['humidity'] # humidity
        wind = x["wind"]["speed"] # wind speed
        chace_of_rain = x["pop"] #chace_of_rain
        pressure = x["main"]["pressure"] #pressure

    print(f"""All the data now for {city_name} :
        Temperature: {temp}°C 
        humidity : {humidity}%
        Wind Speed: {wind} m/s
        Chance of Rain: {chace_of_rain}%
        Pressure: {pressure} hPa
        """)

else:
    print("Failed to retrieve weather data.")
    exit()