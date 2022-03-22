from django.db import models


class GACourse (models.Model):

    title = models.CharField(max_length=128, unique=True)
    date = models.DateField(unique=False, null=True)
    description = models.CharField(max_length=1024, unique=False)

    def __str__(self):
        return self.title

