from django.db import models
from django.utils.translation import gettext_lazy as _

from djangoblog.core.user.models import User


class Tag(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True)
    name = models.CharField(_("name"), max_length=50)

    class Meta:
        db_table = "tag"
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class Post(models.Model):

    id = models.PositiveBigIntegerField(primary_key=True)
    title = models.CharField(_("title"), max_length=200)
    text = models.TextField(_("text"))
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    tags = models.ManyToManyField(
        Tag,
        through="PostTag",
        through_fields=("post", "tag")
    )
    is_deleted = models.BooleanField(default=False, blank=True)
    image = models.ImageField(upload_to="uploads/posts", null=True)

    class Meta:
        db_table = "post"
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")


class PostTag(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        db_table = "post_tags"
        verbose_name = _("Post tag")
        verbose_name_plural = _("Post tags")