#importing the pre made forms to use as the login forms and registration form
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):#Method to render the registration form
	email = forms.EmailField()#Adding an extra field to the form so users can enter thier email address in

	class Meta:
		model = User #Specifying the model 
		fields = ['username', 'email','password1','password2']#The order in which the fields apear on the form

class UserUpdateForm(forms.ModelForm): #The method to update user profile
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email'] #Specifying thr fields to change

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']#Updating the users Profile Image
