# Generated by Django 2.2.17 on 2021-04-04 20:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('film_site', '0026_auto_20210404_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 4, 20, 2, 44, 903147, tzinfo=utc), editable=False),
        ),
    ]
