# Generated by Django 5.0.6 on 2024-06-10 07:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_remove_address_owner_userprofile_address'),
        ('events', '0004_alter_event_created_at_alter_event_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_address', to='accounts.address'),
        ),
    ]
