# Generated by Django 2.2.1 on 2019-06-12 19:52

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmain', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2019, 6, 19, 19, 52, 11, 486046)),
        ),
    ]