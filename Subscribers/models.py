from django.db import models

# Create your models here.
class Subscriber(models.Model):
    subscribers_name=models.CharField(max_length=50)
    subscribers_email=models.EmailField(max_length=50)