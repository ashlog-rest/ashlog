from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from django_random_id_model import RandomIDModel
from encrypted_model_fields.fields import EncryptedCharField
from authentication.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class Project(RandomIDModel):
    """ Model for Projects """
    name = models.CharField(max_length=10)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Log(RandomIDModel):
    """ Model for Logs """
    event = EncryptedCharField(max_length=900, blank=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event


channel_layer = get_channel_layer()


@receiver(post_save, sender=Log)
def log_save(sender, instance, created, **kwargs):
    if created:
        async_to_sync(channel_layer.group_send)(str(instance.project.id), {
            'type': 'new_log',
            'log': instance
        })
