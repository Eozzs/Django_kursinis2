# Generated by Django 5.0.6 on 2024-05-26 19:46

import django.db.models.deletion
import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0031_alter_photo_photo_alter_trip_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='photos/dfimg.jpg', force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[800, 800], upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='trip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='photogallery.trip'),
        ),
        migrations.AlterField(
            model_name='post',
            name='trip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='photogallery.trip'),
        ),
    ]
