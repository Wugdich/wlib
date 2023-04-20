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


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    release_date = models.DateField()
    developer = models.CharField(max_length=30)
    hours_played = models.FloatField()

    def __str__(self):
        return self.title


class Movie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    release_date = models.DateField()
    director = models.CharField(max_length=30)

    # Stutus field staff
    VIEWED = "V"
    NOT_VIEWED = "NV"
    STATUS_CHOICES = [
            (NOT_VIEWED, "Not viewed"),
            (VIEWED, "Viewed"),
            ]
    status = models.CharField(
            max_length=2,
            choices=STATUS_CHOICES,
            default=NOT_VIEWED,
            )

    def __str__(self):
        return self.title
