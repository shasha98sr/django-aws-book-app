from django.db import models

class Book(models.Model):
    title = str(models.CharField(max_length=200))
    author = str(models.CharField(max_length=200))
    year = int(models.IntegerField())

    def __str__(self):
        return self.title