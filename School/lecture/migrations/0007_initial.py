# Generated by Django 4.0.7 on 2022-09-24 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0002_alter_customuser_options_alter_customuser_groups_and_more'),
        ('lecture', '0006_remove_lecture_cat_remove_subject_userclass_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование вопроса')),
                ('ask_true', models.BooleanField(verbose_name='Правильный вопрос')),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название темы')),
                ('subtitle', models.CharField(max_length=255, verbose_name='Подзаголовок')),
                ('full_text', models.TextField(verbose_name='Контент')),
                ('cards', models.ImageField(upload_to='cards/%Y/%m/%d/', verbose_name='Карточки')),
                ('date', models.DateTimeField(verbose_name='Дата добавления')),
                ('is_active', models.BooleanField(null=True, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Лекция',
                'verbose_name_plural': 'Лекции',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_subjects', models.CharField(db_index=True, max_length=150, verbose_name='Предмет')),
                ('subjects_photo', models.ImageField(upload_to='subjects/%Y/%m/%d/', verbose_name='Фотография')),
                ('userClass', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='User.userclass', verbose_name='Класс')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
                'ordering': ['name_subjects'],
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_test', models.CharField(max_length=255, verbose_name='Наименование теста')),
                ('start_date', models.DateTimeField(verbose_name='Дата открытие теста')),
                ('end_date', models.DateTimeField(verbose_name='Дата закрытие теста')),
                ('distance', models.IntegerField(verbose_name='Время прохождения теста(мин)')),
                ('is_active', models.BooleanField(null=True, verbose_name='Опубликован')),
                ('ask', models.ManyToManyField(to='lecture.ask', verbose_name='Вопросы')),
                ('cat_subjects', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lecture.subject', verbose_name='Предмет')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lecture.lecture', verbose_name='Лекция')),
            ],
        ),
        migrations.AddField(
            model_name='lecture',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lecture.subject', verbose_name='Предмет'),
        ),
        migrations.AddField(
            model_name='ask',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lecture.subject', verbose_name='Предмет'),
        ),
    ]