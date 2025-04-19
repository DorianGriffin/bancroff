import requests

url = "http://localhost:50010/api/users"
payload = {
}
headers = {
    "Content-Type": "application/json"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())