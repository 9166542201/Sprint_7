import allure
import requests
from util import Util
from urls import LOGIN


class TestCourierLogin:
    @allure.severity(allure.severity_level.CRITICAL)
    def test_courier_login_valid_data_code_200_contains_id(self, courier):
        response = requests.post(LOGIN,
                                 json={'login': courier['login'], 'password': courier['password']})
        assert response.status_code == 200
        assert isinstance(response.json()['id'], int)

    def test_courier_login_invalid_password_code_404(self, courier):
        response = requests.post(LOGIN,
                                 json={'login': courier['login'], 'password': courier['password'] + '1'})
        assert response.status_code == 404
        assert response.json() == {"code": 404, "message": "Учетная запись не найдена"}

    def test_courier_login_invalid_login_code_404(self, courier):
        response = requests.post(LOGIN,
                                 json={'login': courier['login'] + '1', 'password': courier['password']})
        assert response.status_code == 404
        assert response.json() == {"code": 404, "message": "Учетная запись не найдена"}

    def test_courier_login_empty_login_code_400(self, courier):
        response = requests.post(LOGIN,
                                 json={'login': '', 'password': courier['password']})
        assert response.status_code == 400
        assert response.json() == {"code": 400, "message": "Недостаточно данных для входа"}

    def test_courier_login_empty_password_code_400(self, courier):
        response = requests.post(LOGIN,
                                 json={'login': courier['login'], 'password': ''})
        assert response.status_code == 400
        assert response.json() == {"code": 400, "message": "Недостаточно данных для входа"}

    def test_courier_login_unregistered_courier_code_404(self):
        payload = Util.generate_login_password_name()
        payload.pop('firstName')
        response = requests.post(LOGIN, json=payload)
        assert response.status_code == 404
        assert response.json() == {"code": 404, "message": "Учетная запись не найдена"}
