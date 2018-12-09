from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name = 'возраст')

    def __str__(self):
        fio = ''

        if self.first_name:
            fio += f'{self.first_name.title()}'
            if self.last_name:
                fio += f'{self.last_name.title()}'

        return f'{self.username} ({fio})'
