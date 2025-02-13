import requests
import pytest
from util import Util
from urls import COURIER, LOGIN, ORDERS, CANCEL


@pytest.fixture
def courier():
    # create courier
    courier = Util.generate_login_password_name()
    response = requests.post(COURIER, json=courier)
    yield courier
    # login courier
    response = requests.post(LOGIN,
                             json={'login': courier['login'], 'password': courier['password']})
    courier_id = response.json()['id']
    # delete the Courier
    response = requests.delete(f'{COURIER}/{courier_id}')
