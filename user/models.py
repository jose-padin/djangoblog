from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    UserManager,
)


class BaseUser(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField(_("username"), max_length=150, unique=True)
    first_name = models.CharField(_("first name"), max_length=100)
    last_name = models.CharField(_("last name"), max_length=100)
    email = models.EmailField(_("email"), max_length=200, unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        blank=True,
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        blank=True,
    )
    date_joined = models.DateTimeField(
        _("date joined"),
        default=timezone.now,
        blank=True,
    )
    is_superuser = models.BooleanField(
        _("superuser status"),
        default=False,
        blank=True,
    )

    objects = UserManager()

    class Meta:
        db_table = "user"
        verbose_name = _("User")
        verbose_name_plural = _("Users")
    
    REQUIRED_FIELDS = ("email",)
    USERNAME_FIELD = "username"