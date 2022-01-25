from django.db import models
from django_random_id_model import RandomIDModel
from encrypted_model_fields.fields import EncryptedCharField
from authentication.models import User


class Project(RandomIDModel):
    """ Model for Projects """
    name = models.CharField(max_length=10)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Log(RandomIDModel):
    """ Model for Logs """
    event = EncryptedCharField(max_length=900, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.event
