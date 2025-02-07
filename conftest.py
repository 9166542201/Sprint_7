import requests
import pytest
from util import URL, Util


@pytest.fixture
def courier():
    # create courier
    courier = Util.generate_login_password_name()
    response = requests.post(f'{URL}/api/v1/courier', json=courier)
    assert response.status_code == 201
    assert response.json() == {
        "ok": True
    }
    yield courier
    # login courier
    response = requests.post(f'{URL}/api/v1/courier/login',
                             json={'login': courier['login'], 'password': courier['password']})
    assert response.status_code == 200
    courier_id = response.json()['id']
    assert isinstance(courier_id, int)
    courier['courier_id'] = courier_id
    # delete the Courier
    response = requests.delete(f'{URL}/api/v1/courier/{courier_id}')
    assert response.status_code == 200
    assert response.json() == {
        "ok": True
    }


'''
@pytest.fixture(params=[["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
def orders(request):
    payload = Util.ORDER
    payload['color'] = request.param
    # create order
    response = requests.post(f'{URL}/api/v1/orders', json=payload)
    assert response.status_code == 201
    track_id = response.json()['track']
    assert isinstance(track_id, int)
    response = requests.get(f'{URL}/api/v1/orders/track', params={'t': track_id})
    assert response.status_code == 200
    order_id = response.json()['order']['id']
    assert isinstance(order_id, int)
    yield order_id
    # cancel order
    response = requests.put(f'{URL}/api/v1/orders/cancel', params={"track": track_id})
    assert response.status_code in [200]
'''