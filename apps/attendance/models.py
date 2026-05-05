from django.db import models

class Attendance(models.Model):
    student_id = models.IntegerField()
    date = models.DateField()
    status = models.CharField(max_length=10)

    def __str__(self):
        return str(self.student_id)