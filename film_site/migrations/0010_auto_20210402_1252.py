# Generated by Django 2.2.17 on 2021-04-02 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_site', '0009_auto_20210402_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
    ]
