# Generated by Django 5.0.6 on 2024-05-24 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0007_alter_post_reaction_alter_post_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='album_photo',
            new_name='photo',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_photo',
            new_name='photo',
        ),
    ]
