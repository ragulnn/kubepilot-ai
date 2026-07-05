import requests

response = requests.post(
    "http://127.0.0.1:8000/collect",
    json={
        "question": "Why is nginx restarting?"
    }
)

print("Status:", response.status_code)
print()
print(response.text)
