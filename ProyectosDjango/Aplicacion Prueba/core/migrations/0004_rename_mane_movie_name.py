# Generated by Django 4.0 on 2022-01-15 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_movie_created_movie_modified'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='mane',
            new_name='name',
        ),
    ]
