import sys
import requests
import json

try:
    bitcoin_amount = float(sys.argv[1])
except ValueError:
    sys.exit('Command-line argument is not a number')
except IndexError:
    sys.exit('Missing command-line argument')

# print(bitcoin_amount)

try:
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    r = requests.get(url)
    data = json.loads(r.text)

    usd_rate = data['bpi']['USD']['rate']
    # print(type(usd_rate))
    usd_rate = usd_rate.replace(',', '')
    usd_rate = float(usd_rate)
    # print(usd_rate)
    usd_equivalent = usd_rate * bitcoin_amount
    print(f"${usd_equivalent:,.4f}")


except requests.RequestException as e:
    print(f"Error occurred while making the API request: {e}")