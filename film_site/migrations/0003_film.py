# Generated by Django 2.2.17 on 2021-03-31 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_site', '0002_auto_20210331_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('rating', models.IntegerField(default=0)),
                ('reviews', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('director', models.CharField(max_length=128)),
                ('bio', models.CharField(max_length=500)),
                ('img', models.ImageField(blank=True, upload_to='film_images')),
            ],
            options={
                'verbose_name_plural': 'films',
            },
        ),
    ]