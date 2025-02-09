import allure
import requests
import pytest

from data import ORDER
from urls import ORDERS, CANCEL


class TestCreateOrder:
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order_code_201_track(self, color):
        payload = ORDER
        payload['color'] = color
        # create order
        response = requests.post(ORDERS, json=payload)
        assert response.status_code == 201
        track_id = response.json()['track']
        assert isinstance(track_id, int)
        # cancel order
        requests.put(CANCEL, params={"track": track_id})
