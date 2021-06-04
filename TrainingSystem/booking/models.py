from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE

class Programs(models.Model):
    name = models.CharField(max_length=200)
    isActive = models.BooleanField(blank=True)
<<<<<<< HEAD

    def __str__(self):
        if self.isActive == True:
            return f'{self.name} is active'
        else:
            return f'{self.name} is not active'
=======
>>>>>>> 6cffaa94ad40bce84f543fb4372679cdbb351af7


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
    program = models.ForeignKey(Programs, on_delete=models.CASCADE, default=4)
    image=models.ImageField(default='course.jpg',upload_to='course_photos') #Setting the users profile pic
    

    def __str__(self):
        return f'{self.courseName} is being delivered by {self.host} on {self.start_date}'

class attendees(models.Model):
    departments = [
        ('UI', 'UX & UI'),
        ('IT', 'IT & Support'),
        ('RI', 'Research & Innovation'),
        ('MD', 'Mobile Development'),
        ('WD', 'Web Development'),
        ('CS', 'Cyber Security'),
        ('HR', 'Human Resources'),
        ('FN', 'Finance'),
        ('SA', 'Sales'),
        ('MA', 'Marketing'),
    ]
    courseNeededBy = [
        ('W1M', 'Within 1 Month'),
        ('1-3', '1-3 Months'),
        ('3-6', '3-6 Months'),
        ('6+M', '6+ Months'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, limit_choices_to={'is_staff':True}, on_delete=CASCADE, related_name='manager', blank=True)
    role = models.CharField(max_length=100)
    department = models.CharField(max_length=2, choices=departments)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
<<<<<<< HEAD
    course_due = models.CharField(max_length=3, choices=courseNeededBy)
    your_development = models.CharField(max_length=3000)
    manager_complete = models.CharField(max_length=1000, blank=True)
    approved = models.BooleanField(default=False, blank=True)


=======
>>>>>>> 6cffaa94ad40bce84f543fb4372679cdbb351af7
    def __str__(self):
        return f'{self.user} has booked onto {self.course}'