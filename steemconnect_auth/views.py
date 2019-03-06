#django
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages as ms
from django.contrib.auth import logout, login
from django.views import View
from django.contrib.auth.models import User
from django.conf import settings

# models
from steemconnect_auth.models import SteemConnectUser

# python steemconnect-client
from steemconnect.client import Client

import random

config = settings.STEEMCONNECT_AUTH_CONFIGS

class LoginSignup(View):
    client = Client(client_id = config.get("client_id"),
        redirect_url = config.get("redirect_url"),
        code = config.get("code"),
        scope = config.get("scope")
    )

    def get(self, request, *args, **kwargs):
        code = request.GET["code"]
        tokens = self.client.get_refresh_token(code, config.get("app_secret"))
        username = tokens["username"]
        access_token = tokens["access_token"]
        refresh_token = tokens["refresh_token"]
        user, created = User.objects.get_or_create(username = username)
        if SteemConnectUser.objects.filter(user = user).exists():
            SteemConnectUser.objects.filter(user = user).update(
                code=code,
                access_token=access_token,
                refresh_token=refresh_token
                )
        else:
            SteemConnectUser(
                user=user,
                code=code,
                access_token=access_token,
                refresh_token=refresh_token
                ).save()
        login(request,user, backend="django.contrib.auth.backends.ModelBackend")
        return HttpResponseRedirect(config.get("login_redirect"))


class Logout(View):
    error = "There was an unexpected error while exiting"
    success = "See you again {}"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            ms.success(request,self.success.format(request.user))
            logout(request)
        return HttpResponseRedirect("/")
