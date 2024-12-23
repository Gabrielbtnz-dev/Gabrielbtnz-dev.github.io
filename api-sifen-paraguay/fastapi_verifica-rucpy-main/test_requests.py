import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

print("estado de codigo:", response.status_code)

print("responder contenido:", response.json())