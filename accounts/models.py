from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

from core import settings
from headhunter_app.validators import WordLengthValidator


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE, verbose_name='Пользователь')
    is_employer = models.BooleanField(verbose_name='Работодатель', default=False)
    bio = models.TextField(max_length=500, null=True, blank=True, verbose_name='О себе', validators=[WordLengthValidator(50)])
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class CustomUser(AbstractUser):
    telephone_number = models.IntegerField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False, unique=True)
    image = models.ImageField(upload_to='user_pics', null=True, blank=True, verbose_name='Image')

    USERNAME_FIELD ='username'

    REQUIRED_FIELDS = ['first_name', 'last_name', 'telephone_number', 'image', 'email']

    def __str__(self):
        return self.username
