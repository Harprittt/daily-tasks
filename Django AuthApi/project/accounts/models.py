from django.db import models
     



class Register(models.Model):
    username = models.CharField(max_length=1000)
    first_name = models.CharField(blank=True, null=True, max_length=5000)
    last_name = models.CharField(default=0, blank=False, null=False, max_length=1000)
    email = models.CharField(null=True, blank=True, max_length=1000)
    password = models.CharField(null=True, blank=True, max_length=1000)
 



