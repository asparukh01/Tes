from django.db import models
from django.contrib.auth import get_user_model
from headhunter_app.validators import WordLengthValidator


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE, verbose_name='Пользователь')
    is_employer = models.BooleanField(verbose_name='Работодатель', default=False)
    bio = models.TextField(max_length=500, null=True, blank=True, verbose_name='О себе', validators=[WordLengthValidator(50)])
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
