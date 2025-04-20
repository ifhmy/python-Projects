import requests
import tkinter as tk

def search_weather():
    # get city from laber in tk 
    city_name = city_name_enter.get()  

    # API Key
    api_key = '9a8ccd8134c8957cab64d35a9ffd57d1'

    # url for resonse process
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric"
    
    # send api request
    response = requests.get(url)

    # validate the process
    if response.status_code == 200:
        result_text.delete(1.0, tk.END)   
        print("Weather data retrieved successfully.")
        
        data = response.json()    
        for x in data['list']:
            temp = x['main']['temp']  
            humidity = x['main']['humidity']  
            wind = x["wind"]["speed"]  
            chace_of_rain = x["pop"]  
            pressure = x["main"]["pressure"]  

        # display the weather in label
        result_text.insert(tk.END, f"""Weather data for {city_name}:
            Temperature: {temp}°C
            Humidity: {humidity}%
            Wind Speed: {wind} m/s
            Chance of Rain: {chace_of_rain}%
            Pressure: {pressure} hPa
            """)

    else:
        print("Failed to retrieve weather data.")
        result_text.insert(tk.END, "Failed to retrieve weather data. Please check the city name.\n")

#create window
window = tk.Tk()
window.title("Weather Search")
window.geometry("400x300")  

# ceare lable
city_name_enter = tk.Entry(window, width=30)
city_name_enter.pack(pady=10)  

# create search
search_button = tk.Button(window, text="Search", command=search_weather)
search_button.pack(pady=10)

# create text area
result_text = tk.Text(window, width=50, height=10)
result_text.pack(pady=10) 

#start app
window.mainloop()
