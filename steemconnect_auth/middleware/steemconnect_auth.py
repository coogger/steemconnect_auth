# django
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings


class SteemConnectAuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.steemconnect_auth = settings.STEEMCONNECT_AUTH_CONFIGS