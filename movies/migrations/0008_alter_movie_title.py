# Generated by Django 4.1.3 on 2022-11-25 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_reaction_remove_like_creator_remove_like_review_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(default='', max_length=45),
        ),
    ]
