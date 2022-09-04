from django.db import models
from django.contrib.auth.models import User






class Book(models.Model):
    user = models.ManyToManyField(User)
    book_title = models.CharField(max_length=70)
    book_description = models.TextField(max_length=70)
    publish_date = models.DateField()
    price = models.DecimalField(decimal_places = 2, max_digits = 70, null=True)

    def written_by(self):
        return ",".join([str(p) for p in self.user.all()])

