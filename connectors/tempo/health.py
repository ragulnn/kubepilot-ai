import requests


def tempo_healthy():

    try:

        response = requests.get(

            "http://localhost:3200/ready",

            timeout=3,

        )

        return response.status_code == 200

    except Exception:

        return False
