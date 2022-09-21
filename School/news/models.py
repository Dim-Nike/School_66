from django.db import models


class News(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    subtitle = models.CharField('Анонс', max_length=255)
    full_text = models.TextField('Текст новости')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date']