from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True)
    first_name = models.CharField(_("first name"), max_length=100)
    last_name = models.CharField(_("last name"), max_length=100)
    email = models.EmailField(_("email"), max_length=200)

    class Meta:
        db_table = "user"
        verbose_name = _("User")
        verbose_name_plural = _("Users")
    