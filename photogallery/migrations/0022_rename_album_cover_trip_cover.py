# Generated by Django 5.0.6 on 2024-05-25 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0021_alter_trip_continent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='album_cover',
            new_name='cover',
        ),
    ]
