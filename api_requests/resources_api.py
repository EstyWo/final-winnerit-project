import pytest
import requests
base_url = "https://reqres.in/api"
def test_get_user():
    response = requests.get(f'{base_url}/users/2')
    print(response.json())
    print(response.status_code)
    print(response.reason)
    assert 200 <= response.status_code <= 210
    assert response.status_code == 200
    assert response.json()['data']['id'] == 2
    assert response.json()["data"]['email'] == "janet.weaver@reqres.in"