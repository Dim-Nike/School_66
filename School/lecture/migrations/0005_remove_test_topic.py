# Generated by Django 4.0.7 on 2022-09-24 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0004_test_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='topic',
        ),
    ]