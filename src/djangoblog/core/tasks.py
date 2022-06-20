from celery import shared_task
from django.utils.timezone import now


@shared_task(bind=True)
def publish_post(self):
    print(self)
    self.pub_date = now()
    self.save()