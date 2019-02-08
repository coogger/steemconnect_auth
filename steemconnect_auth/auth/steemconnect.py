# django
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.http import Http404


class SteemConnectBackend:

    def authenticate(self, request, username=None, **kwargs):
        user_model = get_user_model()
        user, created = user_model.objects.get_or_create(username=username)
        return user

    def get_user(self, user_id):
        user_model = get_user_model()
        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None
