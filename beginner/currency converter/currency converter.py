import requests

def convert_currency(amount, from_currency, to_currency):
   
    url = f"https://api.frankfurter.dev/v1/latest?amount={amount}&from={from_currency}&to={to_currency}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: API request failed")
        return None

    data = response.json()

    if "rates" in data and to_currency in data["rates"]:
        return data["rates"][to_currency]
    else:
        return None

print("||||| Currency Converter |||||")
try:
    amount = float(input("Enter the amount you want to convert: "))
    from_currency = input("From Currency (e.g. USD): ").upper().strip()
    to_currency = input("To Currency (e.g. INR): ").upper().strip()

    result = convert_currency(amount, from_currency, to_currency)
    if result:
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
    else:
        print("Conversion failed. Please check currency codes.")
except ValueError:
    print("Invalid amount entered. Please enter a number.")