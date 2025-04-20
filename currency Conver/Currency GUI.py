import tkinter as tk
from tkinter import messagebox
import requests

access_key = '4e6c240286e0dc96a587ec9c11647123'

# Function to fetch data from API
def fetch_data(url):
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

# Function to fetch and display available currencies
def get_currencies():
    currencies_data = fetch_data(f'https://api.currencylayer.com/list?access_key={access_key}')
    if currencies_data:
        return list(currencies_data['currencies'].keys())
    return []

# Function to perform the conversion
def perform_conversion():
    from_currency = from_currency_var.get().upper()
    to_currency = to_currency_var.get().upper()
    amount = amount_var.get()
    
    if from_currency not in currencies or to_currency not in currencies:
        messagebox.showerror("Invalid Input", "Please enter valid currencies.")
        return
    
    if amount <= 0:
        messagebox.showerror("Invalid Input", "Amount must be greater than zero.")
        return
    
    conversion_data = fetch_data(f'https://api.currencylayer.com/convert?access_key={access_key}&from={from_currency}&to={to_currency}&amount={amount}')
    
    if conversion_data:
        result = conversion_data['result']
        result_label.config(text=f"Result: {amount} {from_currency} = {result:.2f} {to_currency}")
    else:
        messagebox.showerror("Conversion Failed", "Unable to perform conversion at the moment.")

# Initialize main window
root = tk.Tk()
root.title("Currency Converter")

# Available currencies
currencies = get_currencies()

# Variables for user input
from_currency_var = tk.StringVar()
to_currency_var = tk.StringVar()
amount_var = tk.DoubleVar()

# UI Elements
tk.Label(root, text="Source Currency:").grid(row=0, column=0, padx=10, pady=5)
from_currency_menu = tk.OptionMenu(root, from_currency_var, *currencies)
from_currency_menu.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Target Currency:").grid(row=1, column=0, padx=10, pady=5)
to_currency_menu = tk.OptionMenu(root, to_currency_var, *currencies)
to_currency_menu.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Amount:").grid(row=2, column=0, padx=10, pady=5)
amount_entry = tk.Entry(root, textvariable=amount_var)
amount_entry.grid(row=2, column=1, padx=10, pady=5)

convert_button = tk.Button(root, text="Convert", command=perform_conversion)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the GUI
root.mainloop()
