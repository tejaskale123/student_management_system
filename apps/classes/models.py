from djongo import models

class Class(models.Model):
    _id = models.ObjectIdField()
    class_name = models.CharField(max_length=100)
    year = models.IntegerField()
    section = models.CharField(max_length=10)