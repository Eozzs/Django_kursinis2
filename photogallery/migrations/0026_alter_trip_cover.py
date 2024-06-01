# Generated by Django 5.0.6 on 2024-05-26 16:47

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0025_alter_trip_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='cover',
            field=django_resized.forms.ResizedImageField(crop=None, default='covers/default.jpg', force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[350, 400], upload_to='covers'),
        ),
    ]
