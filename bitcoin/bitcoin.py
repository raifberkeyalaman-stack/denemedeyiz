import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Missing command-line argument")


try:
    response = requests.get("34d0093b91c878b9af7692256d4d27d3945c88e84c063b6988b3c98aeacb3149")
    response.raise_for_status()
    convert = response.json
except requests.RequestException:
    sys.exit("Request failed")

price = float(convert["data"]["priceUsd"])
value = bitcoins * price

print(f"${value:,.4f}")

