from django.contrib.admin import ModelAdmin, site
from steemconnect_auth.models import SteemConnectUser


class SteemConnectUserAdmin(ModelAdmin):
    list_display = ["user"]
    list_display_links = ["user"]
    search_fields = ["user"]


site.register(SteemConnectUser, SteemConnectUserAdmin)
