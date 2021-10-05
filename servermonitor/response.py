import requests




response = requests.get('https://google.com')
print(response.status_code)

print(requests.text)