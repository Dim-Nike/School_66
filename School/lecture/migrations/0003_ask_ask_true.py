# Generated by Django 4.0.7 on 2022-09-24 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0002_alter_test_distance_ask_test_ask'),
    ]

    operations = [
        migrations.AddField(
            model_name='ask',
            name='ask_true',
            field=models.BooleanField(default=True, verbose_name='Правильный вопрос'),
            preserve_default=False,
        ),
    ]
