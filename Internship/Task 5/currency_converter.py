# Import requests library to fetch API data
import requests

# Display heading
print("===== Currency Converter =====")

# Free Currency Exchange API URL
url = "https://open.er-api.com/v6/latest/USD"

try:
    # Send request to API
    response = requests.get(url)

    # Convert API response into JSON format
    data = response.json()

    # Check if API response is successful
    if data["result"] == "success":

        # Store all currency exchange rates
        rates = data["rates"]

        # Take user input for source currency
        from_currency = input("Enter From Currency (USD, INR, EUR): ").upper()

        # Take user input for target currency
        to_currency = input("Enter To Currency (USD, INR, EUR): ").upper()

        # Take amount to convert
        amount = float(input("Enter Amount: "))

        # Check if entered currencies are valid
        if from_currency in rates and to_currency in rates:

            # Convert entered amount to USD first
            usd_amount = amount / rates[from_currency]

            # Convert USD to target currency
            converted_amount = usd_amount * rates[to_currency]

            # Display final result
            print("\n===== Conversion Result =====")
            print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

        else:
            # If wrong currency code entered
            print("Invalid Currency Code!")

    else:
        # If API data not fetched
        print("Unable to fetch exchange rates.")

except Exception as e:
    # Handle any errors
    print("Error:", e)