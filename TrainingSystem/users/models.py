from django.db import models
from django.contrib.auth.models import User
import PIL
from PIL import Image

class Profile(models.Model): #Creating the profile model
	user = models.OneToOneField(User, on_delete=models.CASCADE) #Setting the user models and also using the .CASCADE so when the user is deleted everything associated with them is deleted
	image=models.ImageField(default='default.jpg',upload_to='profile_photos') #Setting the users profile pic
	manager = models.ForeignKey(User, limit_choices_to={'is_staff':True}, on_delete=models.CASCADE, related_name='manager', null=True)

	def __str__(self):
		return f'{self.user.username} Profile'

	#def save(self, *args, **kwargs):#Saving the users details
		#super().save(*args, **kwargs)
		#img= Image.open(self.image.path)#Saving the images path
		#if img.height>300 or img.width >300:#Automatically resizing the image so it doesnt take up much room on the webserver
			#output_size = (300,300)#Setting the size to 300x300px max
			#img.thumbnail(output_size)
			#img.save(self.image.path)

