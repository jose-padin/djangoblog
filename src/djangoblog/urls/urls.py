from django.contrib import admin
from django.urls import include, re_path

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),

    re_path(r"^", include(("djangoblog.core.authn.urls", "authentication"))),
    re_path(r"^posts/", include(("djangoblog.core.post.urls", "post"))),
]
