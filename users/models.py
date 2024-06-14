from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, max_length=35, verbose_name='почта')
    avatar = models.ImageField(upload_to='users/avatars', verbose_name='аватар', **NULLABLE)
    num_phone = models.CharField(max_length=35, verbose_name='телефон', unique=True)
    country = models.CharField(verbose_name='страна', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'



