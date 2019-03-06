# django
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.http import Http404
from django.contrib.auth import login
import requests

class SteemConnectBackend:

    def authenticate(self, request, username=None, password=None):
        if requests.get(f"https://steemit.com/@{username}").status_code != 200:
            raise Http404
        user_model = get_user_model()
        user, created = user_model.objects.get_or_create(username=username)
        if password is not None and user.is_superuser:
            if user_model(username=username).check_password(password):
                return user
            return None
        return user

    def get_user(self, user_id):
        user_model = get_user_model()
        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None
