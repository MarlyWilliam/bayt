from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=200) 
    country = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title
