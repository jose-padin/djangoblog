from django.contrib import admin

from .models import Post, PostTag, Tag


class PostTag(admin.TabularInline):
    model = PostTag


class TagAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    inlines = [PostTag]


admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)