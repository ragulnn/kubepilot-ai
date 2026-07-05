import requests

response = requests.post(

    "http://localhost:8000/investigate",

    json={

        "question": "Show all nginx pods"

    },

)

print(response.json())
