import sys
import requests

try:
    ...
except requests.RequestException:
    ...


def validate_input(cl_args):
    if len(cl_args) == 2:
        try:
            return float(cl_args[1])
        except:
            pass
    sys.exit("Wrong command line argument.")


def query_coinbase_api_for_bitcoin_price():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    json = response.json()
    price = json["bpi"]["USD"]["rate"]
    price = float(price.replace(",", ""))
    return price


def main():
    n = validate_input(sys.argv)
    price = query_coinbase_api_for_bitcoin_price()
    amount = n * price
    print(f"${amount:,.4f}")


if __name__ == "__main__":
    main()
