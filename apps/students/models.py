from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)   # 👈 ADD THIS
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    class_id = models.IntegerField()