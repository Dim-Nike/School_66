# Generated by Django 4.0.7 on 2022-09-27 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0025_delete_testmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresult',
            name='user',
            field=models.CharField(max_length=255, verbose_name='Пользователь'),
        ),
    ]