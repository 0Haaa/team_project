# Generated by Django 4.1.1 on 2022-10-04 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_background',
            field=models.ImageField(blank=True, unique=True, upload_to='profile_image/', verbose_name='배경사진'),
        ),
    ]
