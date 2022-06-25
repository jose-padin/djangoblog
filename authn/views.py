from pprint import PrettyPrinter

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import (
    LoginView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.views import View

from middleware.login_middleware import login_exempt

from .forms import SignUpForm

print = PrettyPrinter(indent=4).pprint


@login_exempt
class Login(LoginView):
    form_class = AuthenticationForm
    authentication_form = form_class
    template_name = "login.html"
    redirect_authenticated_user = True


@login_exempt
class SignUpView(View):
    form_class = SignUpForm
    template_name = "register.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return redirect("authentication:login")
        else:
            print(form.errors)

        return render(request, self.template_name, {"form": self.form_class})


@login_exempt
class RequestPasswordView(PasswordResetView):
    email_template_name = "request_password_email.html"
    success_url = reverse_lazy("authentication:password_reset_done")
    template_name = "request_password.html"
    title = _("Password reset")


@login_exempt
class PasswordResetDoneView(PasswordResetDoneView):
    template_name = "password_reset_done.html"
    success_url = reverse_lazy("authentication:password_reset_complete")


@login_exempt
class PasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy("authentication:password_reset_complete")
    template_name = "password_reset_confirm.html"
