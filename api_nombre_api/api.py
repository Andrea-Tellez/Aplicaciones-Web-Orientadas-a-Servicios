import requests
import json

result = requests.get('https://developer.twitter.com/es/docs/api/1.1/overview.')
print(result.status_code)
print(result.text)

books = result.json()
print(type(books))

items = books["items"]

coded = json.dumps(items)
decoded = json.loads(coded)

print(decoded[0]["volumeInfo"]["infoLink"])