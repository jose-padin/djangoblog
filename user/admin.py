from django.contrib import admin

from .models import BaseUser


class BaseUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(BaseUser, BaseUserAdmin)