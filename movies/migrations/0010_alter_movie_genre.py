# Generated by Django 4.1.3 on 2022-11-30 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_alter_movie_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genre', to='movies.genre'),
        ),
    ]