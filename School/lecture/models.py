from django.db import models
from django.urls import reverse
from jsonfield import JSONField
from User.models import UserClass, CustomUser


class Lecture(models.Model):
    title = models.CharField('Название темы', max_length=50)
    subtitle = models.CharField('Подзаголовок', max_length=255)
    full_text = models.TextField('Контент')
    cards = models.ImageField('Карточки', upload_to='cards/%Y/%m/%d/')
    date = models.DateTimeField('Дата добавления')
    is_active = models.BooleanField('Опубликовано', null=True)
    cat = models.ForeignKey('Subject', on_delete=models.PROTECT, verbose_name='Предмет')
    test = models.ForeignKey('Test', verbose_name='Наименование теста', on_delete=models.PROTECT, blank=True)

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


class Ask(models.Model):
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ['name']

    name = models.CharField('Наименование вопроса', max_length=255)
    ask_true = models.BooleanField(verbose_name='Правильный вопрос')

    def __str__(self):
        return self.name


class Answer(models.Model):
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['name']

    name = models.CharField(verbose_name='Наименование вопроса', max_length=255)
    ask = models.ManyToManyField(Ask, verbose_name='Список вопросов')
    mark = models.IntegerField(verbose_name='Балл')

    def __str__(self):
        return self.name





class Test(models.Model):
    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
        ordering = ['name_test']

    name_test = models.CharField('Наименование теста', max_length=255)
    start_date = models.DateTimeField('Дата открытие теста')
    end_date = models.DateTimeField('Дата закрытие теста')
    distance = models.IntegerField('Время прохождения теста(мин)')
    is_active = models.BooleanField('Опубликован', null=True)
    answer = models.ManyToManyField(Answer, verbose_name='Вопросы')
    attempts = models.IntegerField(verbose_name='Попытки', max_length=10)

    def __str__(self):
        return self.name_test


class TestResult(models.Model):
    class Meta:
        verbose_name = 'Результаты тестов'
        verbose_name_plural = 'Результаты тестов'
        ordering = ['user']

    test = models.CharField(verbose_name='Наименование теста', max_length=100)
    user = models.CharField(verbose_name='Пользователь', max_length=255)
    class_user = models.IntegerField(verbose_name='Класс')
    date = models.CharField(verbose_name='Дата прохождения теста', max_length=50)
    date_user = models.IntegerField(verbose_name='Время прохождения теста')
    result_test = models.IntegerField(verbose_name='Количество баллов')

    def __str__(self):
        return f'{self.result_test} - {self.user}'




