# Generated by Django 5.0.6 on 2024-06-06 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0043_rename_guest_picture_guestpost_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='reaction',
            field=models.CharField(blank=True, choices=[('Love it', 'Love it'), ('Amazing!', 'Amazing!'), ('Delicious', 'Delicious'), ('Hugs', 'Hugs'), ('You look great!', 'You look great!')], max_length=25, null=True, verbose_name='Reaction'),
        ),
    ]
