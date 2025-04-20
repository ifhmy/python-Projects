import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL الموقع
url = "https://books.toscrape.com/"

# إرسال طلب GET إلى الموقع
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# استخراج بيانات الكتب
books_data = []

# العثور على جميع الكتب في الصفحة
books = soup.find_all('article', class_='product_pod')

# استخراج التفاصيل لكل كتاب
# for book in books:
#     title = book.find('h3').find('a')['title']  # استخراج اسم الكتاب
#     rating = book.find('p', class_='star-rating')['class'][1]  # استخراج التقييم   |  ليه {1} علشان ده ليست محتاجين تاني عنصر فيه
#     price = book.find('p', class_='price_color').text  # استخراج السعر


for book in books:
    title = book.h3.a["title"]
    rating = book.p["class"][1]  # استخراج التقييم
    price = book.find('p', class_='price_color').text
   

    # تخزين البيانات في القائمة
    books_data.append({
        'Title': title,
        'Rating': rating,
        'Price': price
    })

# تحويل البيانات إلى DataFrame
df = pd.DataFrame(books_data)

# تصدير البيانات إلى ملف Excel
df.to_excel('books_data.xlsx', index=False)

print("تم استخراج البيانات بنجاح وتصديرها إلى ملف Excel")
