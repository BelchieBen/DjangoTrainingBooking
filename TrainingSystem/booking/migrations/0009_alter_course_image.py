# Generated by Django 3.2.3 on 2021-06-04 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_alter_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='course.jpg', upload_to='course_photos'),
        ),
    ]
