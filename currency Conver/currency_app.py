import requests

access_key = '4e6c240286e0dc96a587ec9c11647123'

# Function to fetch data from API
def fetch_data(url):
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

# Get available currencies
currencies = fetch_data(f'https://api.currencylayer.com/list?access_key={access_key}')['currencies']

# Display available currencies
print("Available currencies:", ' | '.join(currencies))

# Function to get valid user input
def get_valid_input(prompt):
    while True:
        value = input(prompt).upper()
        if value in currencies:
            return value
        print("Invalid currency. Try again.")

# Get user input for currencies
from_currency = get_valid_input("Enter the source currency (e.g., EUR): ")
to_currency = get_valid_input("Enter the target currency (e.g., GBP): ")

# Validate the amount input
while True:
    try:
        amount = float(input("Enter amount: "))
        if amount > 0:
            break
        print("Amount must be greater than zero.")
    except ValueError:
        print("Invalid amount. Please enter a valid number.")

# Perform conversion
conversion_data = fetch_data(f'https://api.currencylayer.com/convert?access_key={access_key}&from={from_currency}&to={to_currency}&amount={amount}')
if conversion_data:
    print(f"Result: {amount} {from_currency} = {conversion_data['result']:.2f} {to_currency}")
else:
    print("Conversion failed.")
