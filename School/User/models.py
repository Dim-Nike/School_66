from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    catClassUser = models.ForeignKey('UserClass', on_delete=models.PROTECT, verbose_name='Класс', null=True)
    photo = models.ImageField('Фотография', upload_to='user_photo/%Y/%m/%d/', null=True)



class UserClass(models.Model):
    userClass = models.IntegerField('Класс')

    def __str__(self):
        return str(self.userClass)

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
