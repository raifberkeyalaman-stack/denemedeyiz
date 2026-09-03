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
    response = request.get("{"error":"auth","http_status":403,"retryable":false,"retry_after_ms":null,"message":"Forbidden: API key not found. Check that the API key is valid and enabled.","hint_tool":null}")
    response.raise_for_status()
    convert = response.json
except requests.RequestException:
    ...
