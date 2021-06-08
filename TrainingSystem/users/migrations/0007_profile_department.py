# Generated by Django 3.2.3 on 2021-06-08 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='department',
            field=models.CharField(choices=[('UI', 'UX & UI'), ('IT', 'IT & Support'), ('RI', 'Research & Innovation'), ('MD', 'Mobile Development'), ('WD', 'Web Development'), ('CS', 'Cyber Security'), ('HR', 'Human Resources'), ('FN', 'Finance'), ('SA', 'Sales'), ('MA', 'Marketing')], default='HR', max_length=2),
        ),
    ]