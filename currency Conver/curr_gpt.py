import requests

# Define the endpoint and access key
endpoint = 'live'
access_key = '4e6c240286e0dc96a587ec9c11647123'

# Create the full URL for the request
url = f'https://api.currencylayer.com/{endpoint}?access_key={access_key}'

# Send the request to the API
response = requests.get(url)

# Convert the response to JSON format
data = response.json()

# Check if the request was successful
if data.get("success"):
    # Display available currencies for conversion with a space between them
    print("Available currencies for conversion:\n")
    for currency in data["quotes"]:
        print(currency, end='  ')  # Use two spaces between each currency
    print("\n")  # Add a newline at the end for better formatting

    # Get user input for the initial and final currencies, and the amount to convert
    initial_currency = input("Enter the initial currency (e.g., USD): ").upper()
    final_currency = input("Enter the final currency (e.g., GBP): ").upper()
    amount = float(input(f"Enter the amount in {initial_currency} to convert: "))

    # Construct the pair of currencies (e.g., USDGBP)
    currency_pair = f"{initial_currency}{final_currency}"

    # Check if the currency pair is available in the data
    if currency_pair in data["quotes"]:
        rate = data["quotes"].get(currency_pair)  # Get the exchange rate
        converted_amount = amount * rate  # Calculate the converted amount

        # Display the conversion result
        print(f"\nExchange Rate: 1 {initial_currency} = {rate} {final_currency}")
        print(f"{amount} {initial_currency} is equal to {converted_amount} {final_currency}")
    else:
        print(f"\nThe conversion between {initial_currency} and {final_currency} is not available.")

    # Display the source currency and timestamp for reference
    print("\nSource Currency:", data.get("source"))
    print("Timestamp:", data.get("timestamp"))

else:
    print("Error occurred while fetching data:", data.get("error"))
