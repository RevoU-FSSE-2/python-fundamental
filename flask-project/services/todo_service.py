import requests


def get_all_todo():
    # third-party API
    response = requests.get("https://dummyjson.com/todos")
    return response.json()
