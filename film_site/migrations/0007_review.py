# Generated by Django 2.2.17 on 2021-04-01 14:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('film_site', '0006_auto_20210401_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('reviewtext', models.CharField(max_length=500)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film_site.Film')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film_site.UserProfile')),
            ],
        ),
    ]