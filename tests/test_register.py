import requests

payload = {

    "cluster": "kind",

    "hostname": "kind-control-plane",

    "ip": "192.168.1.10",

    "version": "1.0.0",

    "token": "kubepilot",

}

response = requests.post(

    "http://localhost:8000/register",

    json=payload,

)

print(response.json())
