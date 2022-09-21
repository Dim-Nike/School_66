from django.db import models
from django.urls import reverse

from User.models import UserClass


class Lecture(models.Model):
    title = models.CharField('Название темы', max_length=50)
    subtitle = models.CharField('Подзаголовок', max_length=255)
    full_text = models.TextField('Контент')
    cards = models.ImageField('Карточки', upload_to='cards/%Y/%m/%d/')
    date = models.DateTimeField('Дата добавления')
    is_active = models.BooleanField('Опубликовано', null=True)

    cat = models.ForeignKey('Subject', on_delete=models.PROTECT, verbose_name='Предмет')

    # def info_cat(self):
    #     return self.cat.userClass

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Лекция'
        verbose_name_plural = 'Лекции'
        ordering = ['-date']


class Subject(models.Model):
    name_subjects = models.CharField('Предмет', max_length=150, db_index=True)
    subjects_photo = models.ImageField('Фотография', upload_to='subjects/%Y/%m/%d/')
    userClass = models.ForeignKey(UserClass, on_delete=models.PROTECT, verbose_name='Класс')

    def __str__(self):
        return self.name_subjects

    def get_absolute_url(self):
        return reverse('details_lecture', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        ordering = ['name_subjects']


class Test(models.Model):
    name_test = models.CharField('Наименование теста', max_length=255)
    start_date = models.DateTimeField('Дата открытие теста')
    end_date = models.DateTimeField('Дата закрытие теста')
    distance = models.IntegerField('Время прохождения теста')
    is_active = models.BooleanField('Опубликован', null=True)
    cat_subjects = models.ForeignKey('Subject', on_delete=models.PROTECT, verbose_name='Предмет')


# class AskTest:


# class QuestionsTest:
#     name_questions = models.CharField('Вопрос', max_length=255)