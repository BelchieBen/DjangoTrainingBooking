# Generated by Django 3.2.3 on 2021-06-04 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_auto_20210604_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendees',
            name='manager_complete',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]