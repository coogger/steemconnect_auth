from django.db import models
from django.contrib.auth.models import User

# python steemconnect-client
from steemconnect.client import Client

class SteemConnectUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    refresh_token = models.CharField(max_length = 500,help_text = "steemconnect user code / to get get_refresh_token")
    code = models.CharField(max_length = 500,help_text = "steemconnect user code / to get get_refresh_token")
    access_token = models.CharField(max_length = 500,help_text = "steemconnect user access_token to any operations")
    
    def __str__(self):
        return self.user

    def update_access_token(self, secret):
        "This function should be used if access_token expires."
        tokens = Client.get_refresh_token(code=self.code, app_secret=secret)
        access_token = tokens["access_token"]
        SteemConnectUser.objects.filter(user=self.user).update(access_token=access_token)
        return access_token

    @property
    def username(self):
        return self.user.username
