# Generated by Django 5.1.6 on 2025-02-06 14:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
        ('tracking', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='watchstatus',
            constraint=models.UniqueConstraint(fields=('user', 'movie'), name='unique_watch_status'),
        ),
    ]
