from datetime import datetime

from django import forms
from django.utils import timezone

from .models import Post
from .tasks import publish_post


class PostForm(forms.ModelForm):
    scheduled_date = forms.DateField(
        widget=forms.DateInput(
            format=['%d/%m/%Y'],
            attrs={
                'class': 'form-control',
                'placeholder': 'Select a date',
                'type': 'date'
            },
        ),
        required=False,
    )
    scheduled_time = forms.TimeField(
        widget=forms.TimeInput(
            format=['%H:%M'],
            attrs={
                'class': 'form-control',
                'placeholder': 'Select a date',
                'type': 'time'
            },
        ),
        required=False,
    )

    class Meta:
        model = Post
        fields = ("title", "text", "image", "tags")

    def save(self, commit=True):
        obj = Post()
        obj.title =  self.cleaned_data.get("title")
        obj.text =  self.cleaned_data.get("text")
        obj.image =  self.cleaned_data.get("image")
        obj.author = self.author
        obj.save()
        tags = self.data.get("tags", [])

        if tags:
            obj.tags.add(tags)

        _date = self.data.get("scheduled_date", None)
        _time = self.data.get("scheduled_time", None)
        now = timezone.now()

        if _date and not _time:
            time = f"{now.hour}:{now.minute}"

        if _time and not _date:
            date = f"{now.year}-{now.month}-{now.day}"

        if not _date and _time:
            _datetime = f"{now.year}-{now.month} {now.hour} {now.minute}"
        else:
            _datetime = f"{_date} {_time}"

        schedule = datetime.strptime(_datetime, "%Y-%m-%d %H:%M")

        publish_post.s(id=obj.id).apply_async(eta=schedule)

        return obj

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop("author", None)
        return super().__init__(*args, **kwargs)
