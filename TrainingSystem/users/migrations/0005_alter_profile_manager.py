# Generated by Django 3.2.3 on 2021-06-07 08:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0004_alter_profile_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='manager',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, related_name='manager', to=settings.AUTH_USER_MODEL),
        ),
    ]
