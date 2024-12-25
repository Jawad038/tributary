import requests

response = requests.post("http://localhost:8000/record", json={"engine_temperature": 0.3})

print(response.json())  # Afficher la réponse
