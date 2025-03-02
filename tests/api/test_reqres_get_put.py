import pytest
import requests
import allure

from playwright.sync_api import Page, expect

base_url = "https://reqres.in/api"
#
@allure.feature("API test - post")
@allure.story("RepRes API test - post")
@allure.title("API Test - post")
def test_get_list_users():
    url = f'{base_url}/users?page=2'
    with allure.step(f'sending get request to {url}'):
        response = requests.get(url)
    with allure.step(f'validating response of get users list'):
        assert 200 <= response.status_code <= 210
        assert response.status_code == 200
        assert response.json()['data'][0]['id'] == 7
        assert response.json()["data"][0]['email'] == "michael.lawson@reqres.in"

def test_get_single_user():
    url = f'{base_url}/users/2'
    with allure.step(f'sending get request to {url}'):
        response = requests.get(url)
    with allure.step(f'validating response of get a single user'):
        assert 200 <= response.status_code <= 210
        assert response.status_code == 200
        assert response.json()['data']['id'] == 2
        assert response.json()["data"]['email'] == "janet.weaver@reqres.in"


def test_get_user_not_found():
    url = f'{base_url}/users/23'
    with allure.step(f'sending get request to {url}'):
        response = requests.get(url)
    with allure.step(f'validating response of get user not found'):
        assert 400 <= response.status_code <= 410
        assert response.status_code == 404
        assert response.json() == {}
        assert response.reason == "Not Found"


def test_get_list():
    url = f'{base_url}/unknown'
    with allure.step(f'sending get request to {url}'):
        response = requests.get(url)
    with allure.step(f'validating response of get an items list'):
        assert 200 <= response.status_code <= 210
        assert response.status_code == 200
        assert response.json()['data'][0]['id'] == 1
        assert response.json()["data"][0]['name'] == "cerulean"


def test_get_single():
    url = f'{base_url}/unknown/2'
    with allure.step(f'sending get request to {url}'):
        response = requests.get(url)
    with allure.step(f'validating response of get single item'):
        assert 200 <= response.status_code <= 210
        assert response.status_code == 200
        assert response.json()['data']['id'] == 2
        assert response.json()["data"]['name'] == "fuchsia rose"


def test_get_single_not_found():
    url = f'{base_url}/unknown/23'
    with allure.step(f'sending get request to {url}'):
        response = requests.get(url)
    with allure.step(f'validating response of get unknown single item'):
        assert 400 <= response.status_code <= 410
        assert response.status_code == 404
        assert response.json() == {}
        assert response.reason == "Not Found"


def test_update_put_user():
    url = f'{base_url}/users/2'
    new_name = "Dan"
    new_user = {"name": new_name, "job": "Manager"}
    with allure.step(f'sending put request to {url}'):
        response = requests.put(url, json=new_user)
    with allure.step(f'validating response of update (put) user'):
        assert response.status_code == 200
        assert response.json()['name'] == new_name


def test_update_patch_user():
    url = f'{base_url}/users/2'
    new_name = "Dan"
    new_user = {"name": new_name, "job": "Manager"}
    with allure.step(f'sending patch request to {url}'):
        response = requests.patch(url, json=new_user)
    with allure.step(f'validating response of update (patch) user'):
        assert response.status_code == 200
        assert response.json()['name'] == new_name


def test_delete_user():
    url = f'{base_url}/users/2'
    with allure.step(f'sending delete request to {url}'):
        response = requests.delete(url)
    with allure.step(f'validating response of delete user'):
        assert response.status_code == 204
        assert response.reason == 'No Content'


def test_get_delayed_response():
    url = f'{base_url}/users?delay=3'
    with allure.step(f'sending get delayed response to {url}'):
        response = requests.get(url)
    with allure.step(f'validating response of get delayed response'):
        assert 200 <= response.status_code <= 210
        assert response.status_code == 200
        assert response.json()['data'][1]['id'] == 2
        assert response.json()["data"][1]['email'] == "janet.weaver@reqres.in"



