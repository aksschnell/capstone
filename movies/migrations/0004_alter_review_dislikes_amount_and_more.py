# Generated by Django 4.1.3 on 2022-11-23 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='dislikes_amount',
            field=models.IntegerField(default=0, max_length=999),
        ),
        migrations.AlterField(
            model_name='review',
            name='likes_amount',
            field=models.IntegerField(default=0, max_length=999),
        ),
    ]
