from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publish_year = models.DateField()

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

class Game(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    developer = models.CharField(max_length=50)
    hours_played = models.FloatField()

class Movie(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    director = models.CharField(max_length=50)

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

