# Generated by Django 2.2.17 on 2021-04-03 16:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('film_site', '0019_auto_20210403_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 3, 16, 27, 57, 902413, tzinfo=utc), editable=False),
        ),
    ]