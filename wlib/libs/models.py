import datetime

from django.contrib.auth.models import User
from django.db import models

def current_year() -> int:
    return datetime.date.today().year


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    publish_year = models.PositiveIntegerField(
            default=current_year(),
            )

    # Status field staff
    NOT_STARTED = "NS"
    IN_PROGRESS = "IP"
    DONE = "DN"
    STATUS_CHOICES = [
            (NOT_STARTED, "Not started"),
            (IN_PROGRESS, "In progress"),
            (DONE, "Done"),
            ]
    status = models.CharField(
            max_length=2,
            choices=STATUS_CHOICES,
            default=NOT_STARTED,
            )

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(max_length=250, blank=True)
    #avatar = models.ImageField()
    favorite_book = models.ForeignKey(Book, on_delete=models.PROTECT)
    preference = models.CharField(max_length=25)
