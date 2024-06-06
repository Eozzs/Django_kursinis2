# Generated by Django 5.0.6 on 2024-06-04 23:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0038_test'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='reaction',
        ),
        migrations.AlterField(
            model_name='test',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('reaction', models.CharField(blank=True, choices=[('l', 'Love it'), ('a', 'Amazing...'), ('f', 'Delicious'), ('h', 'Hugs'), ('g', 'You look great!')], max_length=1, null=True, verbose_name='Reaction')),
                ('photo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reactions', to='photogallery.photo')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reactions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reaction',
                'verbose_name_plural': 'Reactions',
            },
        ),
    ]