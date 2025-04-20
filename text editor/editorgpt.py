import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# دالة فتح الملف
def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)  # حذف أي محتوى موجود
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
        txt_edit.insert(tk.END, content)  # عرض محتوى الملف في المحرر
    window.title(f"ifhmy Editor - {filepath}")

# دالة حفظ الملف
def save_file():
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "w", encoding="utf-8") as file:
        content = txt_edit.get("1.0", tk.END)
        file.write(content)
    window.title(f"ifhmy Editor - {filepath}")

# إعداد النافذة الرئيسية
window = tk.Tk()
window.title("ifhmy Editor")
window.geometry("800x600")

# إنشاء عناصر الواجهة
txt_edit = tk.Text(window)
frame_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

# أزرار فتح و حفظ
btn_open = tk.Button(frame_buttons, text="Open File", command=open_file)
btn_save = tk.Button(frame_buttons, text="Save File", command=save_file)

# ترتيب الأزرار داخل الإطار
btn_open.grid(row=0, column=0, padx=5, pady=5)
btn_save.grid(row=1, column=0, padx=5, pady=5)

# ترتيب الإطار والمحرر في النافذة
frame_buttons.grid(row=0, column=0, sticky="nw")
txt_edit.grid(row=0, column=1, sticky="nsew")

# جعل المحرر يتمدد مع تغيير حجم النافذة
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# تشغيل التطبيق
window.mainloop()
