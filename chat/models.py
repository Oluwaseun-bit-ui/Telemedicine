from django.db import models
from django.conf import settings
from appointment.models import Appointment

User = settings.AUTH_USER_MODEL

class Message(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} - {self.content[:20]}"