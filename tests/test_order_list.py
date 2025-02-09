import requests
from urls import LOGIN, ORDERS


class TestOrderList:
    def test_show_orders_filtered_by_courier_code_200_empty_list(self, courier):
        response = requests.post(LOGIN,
                                 json={'login': courier['login'], 'password': courier['password']})
        courier_id = response.json()['id']
        response = requests.get(ORDERS, params={'courierId': courier_id})
        assert response.status_code == 200
        orders = response.json()['orders']
        assert isinstance(orders, list) and len(orders) == 0
