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

def test_get_list_users():
    response = requests.get(f'{base_url}/users?page=2')
    print(response.json())
    print(response.status_code)
    print(response.reason)
    assert 200 <= response.status_code <= 210
    assert response.status_code == 200
    assert response.json()['data'][0]['id'] == 7
    assert response.json()["data"][0]['email'] == "michael.lawson@reqres.in"
    # assert response.json()['page'] == 2
    # assert response.json()['total'] == 12

def test_get_user_not_found():
    response = requests.get(f'{base_url}/users/23')
    print(response.json())
    print(response.status_code)
    print(response.reason)
    assert 400 <= response.status_code <= 410
    assert response.status_code == 404
    assert response.json()== {}
    assert response.reason == "Not Found"

def test_get_list():
    response = requests.get(f'{base_url}/unknown')
    print(response.json())
    print(response.status_code)
    print(response.reason)
    assert 200 <= response.status_code <= 210
    assert response.status_code == 200
    assert response.json()['data'][0]['id'] == 1
    assert response.json()["data"][0]['name'] == "cerulean"

def test_get_single():
    response = requests.get(f'{base_url}/unknown/2')
    print(response.json())
    print(response.status_code)
    print(response.reason)
    assert 200 <= response.status_code <= 210
    assert response.status_code == 200
    assert response.json()['data']['id'] == 2
    assert response.json()["data"]['name'] == "fuchsia rose"

def test_get_single_not_found():
    response = requests.get(f'{base_url}/unknown/23')
    print(response.json())
    print(response.status_code)
    print(response.reason)
    assert 400 <= response.status_code <= 410
    assert response.status_code == 404
    assert response.json()== {}
    assert response.reason == "Not Found"

def test_create_user():
    new_name = "Ben"
    new_user = {"name": new_name, "job": "Developer"}
    response = requests.post('https://reqres.in/api/users', json=new_user)

    assert response.status_code == 201
    assert 'id' in response.json()
    assert response.json()['name'] == new_name




