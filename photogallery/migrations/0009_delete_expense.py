# Generated by Django 5.0.6 on 2024-05-24 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0008_rename_album_photo_photo_photo_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Expense',
        ),
    ]