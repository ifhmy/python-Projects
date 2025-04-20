import tkinter as tk
import requests

# API Key
api_key = '9a8ccd8134c8957cab64d35a9ffd57d1'

def search_weather():
    # استلام اسم المدينة المدخل من المستخدم
    city_name = entry.get()
    
    if city_name == "":
        result_text.delete(1.0, tk.END)  # حذف النص القديم في حالة عدم إدخال المدينة
        result_text.insert(tk.END, "Please enter a city name.\n")
        return

    # رابط API للحصول على التوقعات باستخدام اسم المدينة
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric"
    
    # إرسال الطلب إلى API
    response = requests.get(url)

    # تحقق من حالة الاستجابة
    if response.status_code == 200:
        data = response.json()
        # استخراج البيانات وعرضها
        temp = data['list'][0]['main']['temp']
        humidity = data['list'][0]['main']['humidity']
        wind = data['list'][0]["wind"]["speed"]
        rain_chance = data['list'][0]["pop"] * 100  # تحويل إلى نسبة مئوية
        pressure = data['list'][0]["main"]["pressure"]

        # عرض البيانات في نفس النافذة
        result_text.delete(1.0, tk.END)  # مسح النص الحالي
        result_text.insert(tk.END, f"""Weather for {city_name}:
        Temperature: {temp}°C
        Humidity: {humidity}%
        Wind Speed: {wind} m/s
        Chance of Rain: {rain_chance}%
        Pressure: {pressure} hPa
        """)
    else:
        result_text.delete(1.0, tk.END)  # مسح النص الحالي
        result_text.insert(tk.END, "Failed to retrieve weather data. Please check the city name.\n")

# إنشاء نافذة
root = tk.Tk()
root.title("Weather Search")
root.geometry("400x350")

# إضافة تسمية (Label)
label = tk.Label(root, text="Enter City Name:")
label.pack(pady=10)

# إضافة حقل إدخال نص (Text Input Field)
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# إضافة زر (Button)
search_button = tk.Button(root, text="Search", command=search_weather)
search_button.pack(pady=10)

# إضافة مربع نص لعرض النتائج (Text Widget)
result_text = tk.Text(root, width=40, height=10, wrap=tk.WORD)
result_text.pack(pady=10)

# تشغيل واجهة المستخدم
root.mainloop()
