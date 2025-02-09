import random
import string


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
