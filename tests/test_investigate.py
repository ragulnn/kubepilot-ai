import requests

payload = {

    "question": "Show all nginx pods"

}

response = requests.post(

    "http://localhost:8000/investigate",

    json=payload,

)

print(response.json())
