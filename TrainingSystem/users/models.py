from booking.models import attendees
from django.db import models
from django.contrib.auth.models import User
import PIL
from PIL import Image

class Profile(models.Model): #Creating the profile model
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
    divisions = [
        ('OPE','Operations'),
        ('TEC','Technology'),
        ('FIN','Finance'),
        ('MAR','Marketing'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE) #Setting the user models and also using the .CASCADE so when the user is deleted everything associated with them is deleted
    division = models.CharField(max_length=3, choices=divisions, default='OPE')
    department = models.CharField(max_length=2, choices=departments, default='HR')
    manager = models.ForeignKey(User, limit_choices_to={'is_staff':True}, on_delete=models.CASCADE, related_name='manager', null=True)
    image=models.ImageField(default='default.jpg',upload_to='profile_photos') #Setting the users profile pic
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    
	
	# def get_user_completed_courses(self):
	# 	return self.user.objects.filter(attendees.approved == True)

