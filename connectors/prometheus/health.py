import requests


def prometheus_healthy():

    try:

        response = requests.get(

            "http://localhost:9090/-/healthy",

            timeout=3,

        )

        return response.status_code == 200

    except Exception:

        return False
