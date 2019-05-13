from django.conf.urls import url
from django.views.generic.base import RedirectView

#views
from steemconnect_auth.views import Logout, LoginSignup

urlpatterns = [
    url(
        r"^logout/",
        Logout.as_view(),
        name = "logout"
    ),
    url(
        r"^login/",
        RedirectView.as_view(url = LoginSignup.client.get_authorize_url(), permanent=False),
        name = "login"
    ),
    url(
        r"^steemconnect/",
        LoginSignup.as_view(),
        name = "steemconnect"
    ),
]
