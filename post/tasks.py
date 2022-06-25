from celery import shared_task
from django.utils.timezone import now

from post.models import Post


@shared_task(bind=True, name="publish")
def publish_post(self, **kwargs):
    post = Post.objects.get(id=kwargs.get("id", None))
    post.pub_date = now()
    post.save()
