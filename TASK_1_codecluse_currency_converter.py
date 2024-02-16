import requests

def get_exchange_rates(base_currency, target_currencies):
    url = f"https://open.er-api.com/v6/latest/{base_currency}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        rates = data["rates"]
        filtered_rates = {currency: rates[currency] for currency in target_currencies if currency in rates}
        return filtered_rates
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

def main():
    base_currency = input("Enter the base currency code (e.g., USD, EUR): ").upper()
    target_currencies = input("Enter the target currency codes separated by commas (e.g., USD, EUR): ").upper().split(',')
    amount = float(input("Enter the amount to convert: "))

    exchange_rates = get_exchange_rates(base_currency, target_currencies)
    if exchange_rates:
        print("Exchange rates:")
        for currency, rate in exchange_rates.items():
            converted_amount = amount * rate
            print(f"{currency}: {converted_amount}")

if __name__ == "__main__":
    main()
