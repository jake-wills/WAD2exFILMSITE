# Generated by Django 2.2.17 on 2021-04-03 16:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('film_site', '0021_auto_20210403_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 3, 16, 40, 22, 433771, tzinfo=utc), editable=False),
        ),
    ]