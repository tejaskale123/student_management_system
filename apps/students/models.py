from djongo import models
from apps.classes.models import Class


class Student(models.Model):

    _id = models.ObjectIdField()

    name = models.CharField(
        max_length=100
    )

    email = models.EmailField(
        unique=True
    )

    phone = models.CharField(
        max_length=15
    )

    # ✅ FOREIGN KEY RELATION
    student_class = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name='students'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name