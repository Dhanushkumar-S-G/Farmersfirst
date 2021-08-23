from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import User


class Myauth(BaseBackend):
    def authenticate(self, request=None, phone_number=None, password=None):

        try:
            user = User.object.get(pk=int(phone_number))
            login_valid = (user.phone_number == int(phone_number))
            pwd_valid = check_password(password, user.password)
            if login_valid and pwd_valid:
                return user
        except User.DoesNotExist:
            return None

        return None

    def get_user(self, phone_number):
        try:
            return User.object.get(pk=phone_number)
        except User.DoesNotExist:
            return None
