import pytest
import requests
from playwright.sync_api import Page, expect

base_url = "https://reqres.in/api"

# def test_get_list_users(page: Page, users_api):
#     users_api.get_user()


def test_get_list_users():
    response = requests.get(f'{base_url}/users?page=2')
    print(response.json())
    print(response.status_code)
    print(response.reason)
    assert 200 <= response.status_code <= 210
    assert response.status_code == 200
    assert response.json()['data'][0]['id'] == 7
    assert response.json()["data"][0]['email'] == "michael.lawson@reqres.in"

def test_get_user():
    response = requests.get(f'{base_url}/users/2')
    print(response.json())
    print(response.status_code)
    print(response.reason)
    assert 200 <= response.status_code <= 210
    assert response.status_code == 200
    assert response.json()['data']['id'] == 2
    assert response.json()["data"]['email'] == "janet.weaver@reqres.in"


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
    response = requests.post(f'{base_url}/users', json=new_user)
    print(response.json())
    print(response.status_code)
    print(response.reason)
    assert response.status_code == 201
    assert 'id' in response.json()
    assert response.json()['name'] == new_name

def test_update_put_user():
    new_name = "Dan"
    new_user = {"name": new_name, "job": "Manager"}
    response = requests.put(f'{base_url}/users/2', json=new_user)
    print(response.json())
    print(response.status_code)
    print(response.reason)
    assert response.status_code == 200
    assert response.json()['name'] == new_name

def test_update_patch_user():
    new_name = "Dan"
    new_user = {"name": new_name, "job": "Manager"}
    response = requests.patch(f'{base_url}/users/2', json=new_user)
    print(response.json())
    print(response.status_code)
    print(response.reason)
    assert response.status_code == 200
    assert response.json()['name'] == new_name

def test_delete_user():
    response = requests.delete(f'{base_url}/users/2')
    print(response.status_code)
    print(response.reason)
    assert response.status_code == 204
    assert response.reason == 'No Content'

def test_post_register_success():
    register_detail = {"email": "eve.holt@reqres.in", "password": "pistol"}
    response = requests.post(f'{base_url}/register',  json=register_detail)
    print(response.json())
    print(response.status_code)
    print(response.reason)
    assert 200 <= response.status_code <= 210
    assert response.status_code == 200
    assert response.json()['id'] == 4
    assert response.json()['token'] == "QpwL5tke4Pnpja7X4"

def test_post_register_unsuccessful():
    register_detail = {"email": "sydney@fife"}
    response = requests.post(f'{base_url}/register',  json=register_detail)
    print(response.json())
    print(response.status_code)
    print(response.reason)
    assert response.status_code == 400
    assert response.json() == {'error': 'Missing password'}
    assert response.reason == 'Bad Request'

def test_post_login_success():
    register_detail = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post(f'{base_url}/login',  json=register_detail)
    print(response.json())
    print(response.status_code)
    print(response.reason)
    assert 200 <= response.status_code <= 210
    assert response.status_code == 200
    assert response.json()['token'] == "QpwL5tke4Pnpja7X4"

def test_post_login_unsuccessful():
    register_detail = {"email": "peter@klaven"}
    response = requests.post(f'{base_url}/login',  json=register_detail)
    print(response.json())
    print(response.status_code)
    print(response.reason)
    assert response.status_code == 400
    assert response.json() == {'error': 'Missing password'}
    assert response.reason == 'Bad Request'

def test_get_delayed_response():
    response = requests.get(f'{base_url}/users?delay=3')
    print(response.json())
    print(response.status_code)
    print(response.reason)
    assert 200 <= response.status_code <= 210
    assert response.status_code == 200
    assert response.json()['data'][1]['id'] == 2
    assert response.json()["data"][1]['email'] == "janet.weaver@reqres.in"


