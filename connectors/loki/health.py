import requests


def loki_healthy():

    try:

        response = requests.get(

            "http://localhost:3100/ready",

            timeout=5,

        )

        return response.status_code == 200

    except Exception:

        return False
