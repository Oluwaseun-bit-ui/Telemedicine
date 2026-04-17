from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    hospital = models.CharField(max_length=255)
    years_of_experience = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name