# Generated by Django 4.2.6 on 2024-02-14 08:12

import django.core.validators
from django.db import migrations, models
import video.models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_alter_crimevideos_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crimevideos',
            name='video',
            field=models.FileField(upload_to='crime_videos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'mp4', 'mkv', 'webm']), video.models.validate_video_size]),
        ),
    ]
