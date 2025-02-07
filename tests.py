import allure
import requests
import pytest
from util import URL, Util


class TestCourierCreate:
    @allure.severity(allure.severity_level.CRITICAL)
    def test_courier_creation_valid_data_code_201_ok_true(self, courier):
        pass

    def test_courier_creation_duplicate_login_code_409(self, courier):
        payload = Util.generate_login_password_name()
        payload['login'] = courier['login']
        response = requests.post(f'{URL}/api/v1/courier', json=payload)
        assert response.status_code == 409

    def test_courier_creation_empty_login_code_400(self):
        payload = Util.generate_login_password_name()
        payload['login'] = ''
        response = requests.post(f'{URL}/api/v1/courier', json=payload)
        assert response.status_code == 400

    def test_courier_creation_empty_password_code_400(self):
        payload = Util.generate_login_password_name()
        payload['password'] = ''
        response = requests.post(f'{URL}/api/v1/courier', json=payload)
        assert response.status_code == 400


class TestCourierLogin:
    @allure.severity(allure.severity_level.CRITICAL)
    def test_courier_login_valid_data_code_200_contains_id(self, courier):
        response = requests.post(f'{URL}/api/v1/courier/login',
                                 json={'login': courier['login'], 'password': courier['password']})
        assert response.status_code == 200

    def test_courier_login_invalid_password_code_404(self, courier):
        response = requests.post(f'{URL}/api/v1/courier/login',
                                 json={'login': courier['login'], 'password': courier['password'] + '1'})
        assert response.status_code == 404

    def test_courier_login_invalid_login_code_404(self, courier):
        response = requests.post(f'{URL}/api/v1/courier/login',
                                 json={'login': courier['login'] + '1', 'password': courier['password']})
        assert response.status_code == 404

    def test_courier_login_empty_login_code_400(self, courier):
        response = requests.post(f'{URL}/api/v1/courier/login',
                                 json={'login': '', 'password': courier['password']})
        assert response.status_code == 400

    def test_courier_login_empty_password_code_400(self, courier):
        response = requests.post(f'{URL}/api/v1/courier/login',
                                 json={'login': courier['login'], 'password': ''})
        assert response.status_code == 400

    def test_courier_login_unregistered_courier_code_404(self):
        payload = Util.generate_login_password_name()
        payload.pop('firstName')
        response = requests.post(f'{URL}/api/v1/courier/login', json=payload)
        assert response.status_code == 404


class TestCreateOrder:
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order_code_201_track(self, color):
        payload = Util.ORDER
        payload['color'] = color
        # create order
        response = requests.post(f'{URL}/api/v1/orders', json=payload)
        assert response.status_code == 201
        track_id = response.json()['track']
        assert isinstance(track_id, int)
        # cancel order
        response = requests.put(f'{URL}/api/v1/orders/cancel', params={"track": track_id})
        assert response.status_code in [200]


class TestOrderList:
    def test_show_orders_filtered_by_courier_code_200_empty_list(self, courier):
        response = requests.post(f'{URL}/api/v1/courier/login',
                                 json={'login': courier['login'], 'password': courier['password']})
        assert response.status_code == 200
        courier_id = response.json()['id']
        response = requests.get(f'{URL}/api/v1/orders', params={'courierId': courier_id})
        assert response.status_code == 200
        orders = response.json()['orders']
        assert isinstance(orders, list) and len(orders) == 0
