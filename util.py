import random
import string

URL = 'http://qa-scooter.praktikum-services.ru'


class Util:
    @staticmethod
    def generate_login_password_name():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        return {
            "login": 'CVN' + generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

    ORDER = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Moscow, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    }
