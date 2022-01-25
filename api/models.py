from django.db import models
from authentication.models import User


class Log(models.Model):
    event = models.CharField(max_length=900, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.event
