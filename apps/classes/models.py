from django.db import models

class Class(models.Model):
    class_name = models.CharField(max_length=100)
    year = models.IntegerField()
    section = models.CharField(max_length=10)