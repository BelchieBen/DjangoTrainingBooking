# Generated by Django 3.2.3 on 2021-06-08 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0016_remove_attendees_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendees',
            name='blankField',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]