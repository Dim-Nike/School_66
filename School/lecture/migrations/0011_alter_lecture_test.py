# Generated by Django 4.0.7 on 2022-09-24 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0010_remove_test_cat_subjects_remove_test_topic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='test',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='lecture.test', verbose_name='Наименование теста'),
        ),
    ]
