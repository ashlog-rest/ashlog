from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from authentication.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """ Model for user profile """
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(
        _('username'), max_length=30, unique=True, primary_key=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email',
    ]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """ Returns the first name plus the last name """
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.username
