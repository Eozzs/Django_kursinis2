# Generated by Django 5.0.6 on 2024-05-26 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0029_alter_trip_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='cover',
            field=models.ImageField(null=True, upload_to='covers'),
        ),
    ]