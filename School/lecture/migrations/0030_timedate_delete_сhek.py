# Generated by Django 4.0.7 on 2022-10-03 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0029_сhek'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='сhek',
        ),
    ]
