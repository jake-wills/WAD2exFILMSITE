# Generated by Django 2.2.17 on 2021-04-04 20:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('film_site', '0028_auto_20210404_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 4, 20, 44, 26, 350155, tzinfo=utc), editable=False),
        ),
    ]
