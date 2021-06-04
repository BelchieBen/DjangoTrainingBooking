from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from users.models import Profile

def register(request):#Function to register the new user
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)#Loading the form
		if form.is_valid():
			form.save()#Saving the form if its valid
			username = form.cleaned_data.get('username')#Extracting the username from the form
			return redirect('login')#Redirecting the user to log in
	else:
		form = UserRegistrationForm()
	return render(request, 'users/register.html', {'form':form})
	
@login_required #Ensuring that the user is logged in to access this function to edit thier profile
def profile(request):
	if request.method == 'POST':
		Uform=UserUpdateForm(request.POST,instance=request.user)#Setting the varibles so the user who request using POST is saved
		Pform=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)#Comparing the instance of the requested user to the profile they want to update
		if Uform.is_valid() and Pform.is_valid():
			Uform.save()
			Pform.save()
			messages.success(request, f'Your account has been updated!')#Sucsess message to let user know thier profile has been updated.
			return redirect('profile')#Redirecting the user to thier profile page 
	else:
		Uform=UserUpdateForm(instance=request.user)
		Pform=ProfileUpdateForm(instance=request.user.profile)

	context={
	'Uform':Uform, 
	'Pform':Pform
	}
	return render(request,'users/profile.html',context)
	

