import requests
import sys
import json

response = requests.get("https://itunes.apple.com/search?term=Mor%20ve%20%C3%96tesi&entity=song&limit=20")
convert = response.json()
#print(json.dumps(convert, indent=2))
for result in convert["results"]:
    print(result["trackName"])
