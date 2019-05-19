# django
from django.contrib.auth import get_user_model

class SteemConnectBackend:

    def authenticate(self, request, username=None, password=None):
        username = username.lower()

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
