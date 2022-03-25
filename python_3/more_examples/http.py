import requests

r = requests.get("https://swapi.dev/api/people/1")

print('Status Code:')
print(r.status_code)
# print(r)