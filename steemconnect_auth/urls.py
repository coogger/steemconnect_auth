from django.urls import path
from django.views.generic.base import RedirectView

#views
from steemconnect_auth.views import Logout, LoginSignup

urlpatterns = [
    path(
        "login/",
        LoginSignup.as_view(),
        name = "login-via-steemconnect"
    ),
    path(
        "logout/",
        Logout.as_view(),
        name = "logout"
    ),
    path(
        "",
        RedirectView.as_view(url=LoginSignup.client.get_authorize_url(), permanent=False),
        name = "redirect-steemconnect"
    ),
]
