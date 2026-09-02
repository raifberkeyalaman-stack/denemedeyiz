import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except requests.RequestException:
    ...
