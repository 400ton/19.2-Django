from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, max_length=35, verbose_name='почта')
    avatar = models.ImageField(upload_to='users/avatars', verbose_name='аватар', **NULLABLE)
    num_phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    country = models.CharField(verbose_name='страна', **NULLABLE)

    verification_code = models.CharField(max_length=100, verbose_name='код', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} "

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
