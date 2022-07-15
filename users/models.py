from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

from users.managers import UserManager


class CustomUser(AbstractUser):
    """Пользователь"""
    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )
    email = models.EmailField(verbose_name='Email', unique=True)
    status = models.CharField(verbose_name='Статус', max_length=500, blank=True, null=True)
    birth_day = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    gender = models.CharField(verbose_name='Пол', max_length=6, choices=GENDER, default='male')
    bio = models.TextField(verbose_name='Био', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Когда добавлен', auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    objects = UserManager()

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
