from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE

class availablePrograms(models.Model):
    name = models.CharField(max_length=200)


class Course(models.Model):
    staff=(
        ('CAL', 'CALUM'),
        ('YAN', 'YANNA'),
        ('HAN', 'HANNA'),
        ('EXT', 'EXTERNAL'),
    )
    courseNumber = models.IntegerField()
    courseName = models.CharField(max_length=200)
    courseDesc = models.CharField(max_length=500)
    host = models.CharField(max_length=3, choices=staff)
    min_participants = models.IntegerField()
    max_participants = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f'{self.courseName} is being delivered by {self.host} on {self.start_date}'

class attendees(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} has booked onto {self.course}'