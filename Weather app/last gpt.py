import requests
import tkinter as tk

def search_weather():
    """
    هذه الدالة تقوم بالبحث عن الطقس لمدينة معينة باستخدام OpenWeatherMap API.
    """
    # الحصول على اسم المدينة من حقل الإدخال
    city_name = city_name_enter.get()

    # تحقق إذا كان المدخل فارغًا، وإذا كان كذلك إظهار رسالة تنبيه
    if not city_name.strip():
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please enter a city name.\n")
        return

    # مفتاح API للوصول إلى بيانات الطقس
    api_key = '9a8ccd8134c8957cab64d35a9ffd57d1'

    # بناء رابط API باستخدام اسم المدينة والمفتاح API
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric"
    
    try:
        # إرسال الطلب إلى API للحصول على بيانات الطقس
        response = requests.get(url)

        # التحقق من حالة الاستجابة (إذا كانت 200 يعني أن الطلب تم بنجاح)
        if response.status_code == 200:
            # مسح محتويات مربع النص قبل إضافة البيانات الجديدة
            result_text.delete(1.0, tk.END)
            print("Weather data retrieved successfully.")

            # تحويل الاستجابة إلى JSON
            data = response.json()

            # استخراج البيانات المطلوبة من استجابة API
            for x in data['list']:
                temp = x['main']['temp']  # درجة الحرارة
                humidity = x['main']['humidity']  # الرطوبة
                wind = x["wind"]["speed"]  # سرعة الرياح
                chace_of_rain = x["pop"]  # احتمال الأمطار
                pressure = x["main"]["pressure"]  # الضغط الجوي

            # عرض البيانات في مربع النص في واجهة المستخدم
            result_text.insert(tk.END, f"""Weather data for {city_name}:
            Temperature: {temp}°C
            Humidity: {humidity}%
            Wind Speed: {wind} m/s
            Chance of Rain: {chace_of_rain}%
            Pressure: {pressure} hPa
            """)

        else:
            # إذا فشل الطلب وكان رمز الحالة غير 200، إظهار رسالة خطأ
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, f"Failed to retrieve weather data for {city_name}. Please check the city name.\n")

    except requests.exceptions.RequestException as e:
        # إذا حدث خطأ في الاتصال بالإنترنت أو أثناء إرسال الطلب
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error occurred: {e}\n")

# إنشاء نافذة التطبيق باستخدام Tkinter
window = tk.Tk()
window.title("Weather Search")  # تعيين عنوان النافذة
window.geometry("500x400")  # حجم النافذة

# إضافة إطار لتحسين تنسيق العناصر
frame = tk.Frame(window, bg='#2C3E50', padx=20, pady=20)
frame.pack(fill="both", expand=True)

# إنشاء حقل إدخال نص لاسم المدينة
city_name_enter = tk.Entry(frame, width=30, font=('Arial', 14))
city_name_enter.pack(pady=10)

# إنشاء زر البحث الذي سيقوم بتشغيل الدالة `search_weather()` عند الضغط عليه
search_button = tk.Button(frame, text="Search", command=search_weather, font=('Arial', 12), bg='#3498DB', fg='white', bd=0, relief="solid", width=20, height=2)
search_button.pack(pady=10)

# إضافة مربع نص لعرض نتائج الطقس أو رسائل الخطأ
result_text = tk.Text(frame, width=50, height=10, font=('Arial', 12), bg='#ECF0F1', fg='#2C3E50', wrap=tk.WORD, bd=0)
result_text.pack(pady=10)

# إضافة تذييل مع تصميم احترافي
footer_label = tk.Label(window, text="Weather Search App", font=('Arial', 10), bg='#2C3E50', fg='white')
footer_label.pack(side="bottom", fill="x", pady=5)

# تشغيل واجهة المستخدم
window.mainloop()
