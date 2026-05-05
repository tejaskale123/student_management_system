from djongo import models

class Attendance(models.Model):
    _id = models.ObjectIdField()
    student_id = models.CharField(max_length=50)
    date = models.DateField()
    status = models.CharField(max_length=10)

    def __str__(self):
        return str(self.student_id)