from django.db import models

from djangotoolbox.fields import ListField


class shouts(models.Model):
    title = models.CharField()
    text = models.TextField()
    tags = ListField()
    comments = ListField()