# Generated by Django 5.0.6 on 2024-06-05 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0041_guestbook_guestpost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guestpost',
            old_name='theme',
            new_name='guestbook',
        ),
    ]