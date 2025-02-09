import allure
import requests
from util import Util
from urls import COURIER


class TestCourierCreate:
    @allure.severity(allure.severity_level.CRITICAL)
    def test_courier_creation_valid_data_code_201_ok_true(self):
        response = requests.post(COURIER, json=Util.generate_login_password_name())
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    def test_courier_creation_duplicate_login_code_409(self, courier):
        payload = Util.generate_login_password_name()
        payload['login'] = courier['login']
        response = requests.post(COURIER, json=payload)
        assert response.status_code == 409
        assert response.json() == {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}

    def test_courier_creation_empty_login_code_400(self):
        payload = Util.generate_login_password_name()
        payload['login'] = ''
        response = requests.post(COURIER, json=payload)
        assert response.status_code == 400
        assert response.json() == {"code": 400, "message": "Недостаточно данных для создания учетной записи"}

    def test_courier_creation_empty_password_code_400(self):
        payload = Util.generate_login_password_name()
        payload['password'] = ''
        response = requests.post(COURIER, json=payload)
        assert response.status_code == 400
        assert response.json() == {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
