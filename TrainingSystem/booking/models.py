from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Programs(models.Model):
    name = models.CharField(max_length=200)
    isActive = models.BooleanField(blank=True)

    def __str__(self):
        if self.isActive == True:
            return f'{self.name} is active'
        else:
            return f'{self.name} is not active'


class Course(models.Model):
    staff=(
        ('CAL', 'CALUM'),
        ('YAN', 'YANNA'),
        ('HAN', 'HANNA'),
        ('EXT', 'EXTERNAL'),
    )
    divisions = (
        ('GLO','Company Wide'),
        ('OPE','Operations'),
        ('TEC','Technology'),
        ('FIN','Finance'),
        ('MAR','Marketing'),
    )
    courseNumber = models.IntegerField()
    courseName = models.CharField(max_length=200)
    courseDesc = models.CharField(max_length=500)
    host = models.CharField(max_length=3, choices=staff)
    min_participants = models.IntegerField()
    max_participants = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    program = models.ForeignKey(Programs, on_delete=models.CASCADE, default=4)
    division_access = models.CharField(max_length=3, choices=divisions, default='GLO')
    image=models.ImageField(default='course.jpg',upload_to='course_photos') #Setting the users profile pic
    course_completed = models.BooleanField(blank=True)
    

    def __str__(self):
        return f'{self.courseName} is being delivered by {self.host} on {self.start_date}'

    def get_approved_bookings(self):
        return self.attendees_set.filter(status='APR')

class attendees(models.Model):
    courseNeededBy = [
        ('W1M', 'Within 1 Month'),
        ('1-3', '1-3 Months'),
        ('3-6', '3-6 Months'),
        ('6+M', '6+ Months'),
    ]
    statuses = [
        ('PEN', 'Pending'),
        ('APR', 'Approved'),
        ('REJ', 'Rejected'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    role = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_due = models.CharField(max_length=3, choices=courseNeededBy)
    your_development = models.CharField(max_length=3000)
    status = models.CharField(max_length=3, choices=statuses, default='PEN')


    def __str__(self):
        return f'{self.user} has booked onto {self.course}'