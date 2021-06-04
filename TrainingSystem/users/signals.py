from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User) #This is a signal that says when the user is saved send a signal to the function
def create_profile(sender, instance, created, **kwargs): #Function to create a new profile automatically as soon as a new user is created
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User) #This is a signal that says when the user is saved send a signal to the function
def save_profile(sender, instance, **kwargs): #Function to save the new profile created 
		instance.profile.save() 