import pytest
import requests
import allure

base_url = "https://reqres.in/api"

@allure.feature("API test - get & put")
@allure.story("RepRes API test - get & put")
@allure.title("API Test - get & put")

def test_create_user():
    url = f'{base_url}/users?page=2'
    new_name = "Ben"
    new_user = {"name": new_name, "job": "Developer"}
    with allure.step(f'sending post request to {url}'):
        response = requests.post(f'{base_url}/users', json=new_user)
    with allure.step(f'validating response of post - create a user'):
        assert response.status_code == 201
        assert 'id' in response.json()
        assert response.json()['name'] == new_name

def test_post_register_success():
    register_detail = {"email": "eve.holt@reqres.in", "password": "pistol"}
    with allure.step(f'sending post register request to {base_url}'):
        response = requests.post(f'{base_url}/register',  json=register_detail)
    with allure.step(f'validating response of post register success'):
        assert 200 <= response.status_code <= 210
        assert response.status_code == 200
        assert response.json()['id'] == 4
        assert response.json()['token'] == "QpwL5tke4Pnpja7X4"


def test_post_register_unsuccessful():
    register_detail = {"email": "sydney@fife"}
    with allure.step(f'sending post register unsuccessful request to {base_url}'):
        response = requests.post(f'{base_url}/register',  json=register_detail)
    with allure.step(f'validating response of post register unsuccessful'):
        assert response.status_code == 400
        assert response.json() == {'error': 'Missing password'}
        assert response.reason == 'Bad Request'


def test_post_login_success():
    register_detail = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    with allure.step(f'sending post login successful request to {base_url}'):
        response = requests.post(f'{base_url}/login',  json=register_detail)
    with allure.step(f'validating response of post login successful'):
        assert 200 <= response.status_code <= 210
        assert response.status_code == 200
        assert response.json()['token'] == "QpwL5tke4Pnpja7X4"


def test_post_login_unsuccessful():
    register_detail = {"email": "peter@klaven"}
    with allure.step(f'sending post login unsuccessful request to {base_url}'):
        response = requests.post(f'{base_url}/login',  json=register_detail)
    with allure.step(f'validating response of post login unsuccessful'):
        assert response.status_code == 400
        assert response.json() == {'error': 'Missing password'}
        assert response.reason == 'Bad Request'






