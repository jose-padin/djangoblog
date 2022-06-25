from re import template
from django.contrib.auth.views import LogoutView, PasswordResetCompleteView
from django.urls import path, re_path

from .views import (
    Login,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    RequestPasswordView,
    SignUpView,
)


urlpatterns = [
    # re_path(r"^login/$", Login.as_view(), name="login"),
    re_path(r"^$", Login.as_view(), name="login"),
    re_path(r"^logout/$", LogoutView.as_view(), name="logout"),
    re_path(r"^signup/$", SignUpView.as_view(), name="signup"),

    # NOTE: password reset
    re_path(r"^recovery/$", RequestPasswordView.as_view(), name="request_password"),
    re_path(r"^reset_done/$", PasswordResetDoneView.as_view(), name="password_reset_done"),
    re_path(r"^reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,40})", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    re_path(r"^reset_complete/$", PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete"),
]
