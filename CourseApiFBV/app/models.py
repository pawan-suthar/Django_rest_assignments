from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    discount = models.CharField(default=0,max_length=10)
    duration = models.FloatField()
    authorname = models.CharField(max_length=100)

    def __str__(self):
        return self.name
