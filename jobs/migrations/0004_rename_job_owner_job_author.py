# Generated by Django 5.0.6 on 2024-06-09 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_job_media'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='job_owner',
            new_name='author',
        ),
    ]
