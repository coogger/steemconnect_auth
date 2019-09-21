# django
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class SteemConnectAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.steemconnect_auth = settings.STEEMCONNECT_AUTH_CONFIGS
