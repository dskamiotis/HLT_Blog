# Generated by Django 3.0.4 on 2020-03-22 20:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200322_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 22, 20, 25, 18, 16545, tzinfo=utc)),
        ),
    ]
