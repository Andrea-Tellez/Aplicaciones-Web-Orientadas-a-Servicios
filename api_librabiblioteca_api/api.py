import requests
import json

result = requests.get('https://www.etnassoft.com/api/v1/get/?book_author=adrian_paenza')
print(result.status_code)

print(result.text)

books = result.json()

encode = json.dumps(books)
decoded =json.loads(encode) 

print(decoded[0]["title"])
print(decoded[0]["author"])
print(decoded[0]["content"])
