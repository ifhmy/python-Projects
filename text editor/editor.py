import tkinter as tk
from tkinter.filedialog import askopenfilename


def open_file():
    filepath = askopenfilename(
        fileytypes=[("Text files", "*.txt"), ("All files", "*.*")])

def save_file():
    print("saving file")
    




window = tk.Tk()
window.title("ifhmy Editor")

window.geometry("800x600")

txt_edit = tk.Text(window)
frame_buttons = tk.Frame(window , relief=tk.RAISED )
# عملنا هنا الازرار ولكن لم تظهر الا اذا قمنا بتحديد اماكنها
# باستخدام grid
btn_open = tk.Button (frame_buttons, text="Open file" , command=open_file)

btn_save = tk.Button (frame_buttons, text="save file" , command= save_file)

# هنا قمنا بتحديد مكان النصوص في الواجهة باستخدام grid
btn_open.grid(row=0, column=0, padx=5, pady=5)
btn_save.grid(row=1, column=0, padx=5, pady=5)

# هنا قمنا بتحديد مكان النصوص في الواجهة باستخدام grid
frame_buttons.grid(row=0, column=0, sticky="nw")

txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()