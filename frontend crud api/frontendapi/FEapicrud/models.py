from django.db import models


class Novel(models.Model):

    title = models.CharField(max_length=100, blank = True)
    author = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=500, blank=True)
    publisher = models.CharField(max_length=50, blank=True)


    def __str__(self):
        return self.title