# Generated by Django 4.0.7 on 2022-09-26 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0021_alter_testresult_result_test_alter_testresult_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(verbose_name='Баллы')),
            ],
        ),
    ]
