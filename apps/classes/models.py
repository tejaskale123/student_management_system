from djongo import models


class Class(models.Model):

    _id = models.ObjectIdField()

    class_name = models.CharField(
        max_length=100
    )

    year = models.IntegerField()

    section = models.CharField(
        max_length=10
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.class_name} - {self.section}"