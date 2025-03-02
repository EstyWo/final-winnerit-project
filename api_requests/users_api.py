import pytest
import requests
from playwright.sync_api import Page, expect

api_url = "https://reqres.in/api/users/"

# URL + endpoint + path
# users/2

class UsersApi:

    def __init__(self):
        pass


    def get_user(self, endpoint:str):

        response = requests.get(f'{api_url}/{endpoint}')
        print(response.json())
        print(response.status_code)
        print(response.reason)
        assert 200 <= response.status_code <= 210
        assert response.status_code == 200
        assert response.json()['data']['id'] == 2
        assert response.json()['data']['email'] == "janet.weaver@reqres.in"
