# Generated by Django 4.1.7 on 2023-03-31 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0002_remove_audio_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='audio',
            field=models.FileField(default=2, upload_to='audio/'),
            preserve_default=False,
        ),
    ]
