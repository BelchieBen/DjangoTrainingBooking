from users.models import Profile
from django import urls
from django.db.models import manager
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from .models import attendees, Course, Programs
from django.views.generic.detail import DetailView
from django.views.generic import View, CreateView, FormView
from .forms import addCourseForm, addprogramForm, bookCourse
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings
import pandas as pd

def dashboard(request):
    #Getting the database objects
    attendents = attendees.objects.all()
    courses = Course.objects.all()
    programs = Programs.objects.all()
    userData = User.objects.all()

    #Need all this for the user data table
    UserDetails ={} #Setting a dict to create a DataFrame from 
    for u in userData: #Looping through the user object
        testlist = [] #Starting empty list
        userID = u.id #Getting the user ID
        testlist.append(userID) #Appending the list with the ID
        UserDetails[userID] = userID #Adding the user ID to the dict as a key and value

        userName = u.username
        testlist.append(userName)
        UserDetails[userID] = testlist #Adding the username to dict as a value with the user ID as a key

        userEmail = u.email
        testlist.append(userEmail)
        UserDetails[userID]= testlist

        userDepartment = u.profile.department
        testlist.append(userDepartment)
        UserDetails[userID] = testlist

        userManager = u.profile.manager #Going through the user profile to get manager, user is a 1 to 1 relationship so I can access attributes by seperating them with .'s
        testlist.append(userManager)
        UserDetails[userID] = testlist

        totalCompleteCourse = u.user.filter(course__course_completed=True).count() #Creating a query on the user object to count the number of courses completed, this is a 1 to many relationship through forign key so to access those atributes in a queryset use x__y
        testlist.append(totalCompleteCourse)
        UserDetails[userID] = testlist

        completedCourses = u.user.filter(status='APR').filter(course__course_completed=True).values_list('course__courseName', flat=True) #Same as above query but this time i use .values_list to only get the values of the queryset which in this case is the courseName
        completedList = list(completedCourses)#Turning the queryset into a list
        testlist.append(completedList)
        UserDetails[userID] = testlist
    
    df = pd.DataFrame.from_dict(UserDetails, orient='index', columns=['EmployeeNumber','Name', 'Email','Department','Manager','TotalCoursesCompleted', 'CoursesCompleted']) #Creating 1 DataFrame from the dict
    allData=[] #This list will be passed to the HTML template
    for i in range(df.shape[0]): #For loop to get data from DF but keep column structure 
        temp = df.iloc[i]
        allData.append(dict(temp))
    
    #Needed to get data for chart on Dashboard
    emptDict = {} #New dict to hold approved bookings
    for event in courses: #Looping through the courses object
        attendies =  event.attendees_set.filter(status='APR').count() #Getting attendees through reverse lookup on forign key which is attendees_set.filter() and then counting the values
        emptDict[event.courseName] = attendies

    #Lists for the chart
    valueList = []
    labels = []
    for key,value in emptDict.items():#Getting the keys and values seperate from the dict
        valueList.append(value)
        labels.append(str(key))

    context = {'attendees' : attendents, 'course': courses, 'programs': programs, 'attendants':emptDict, 'valueList':valueList, 'labels':labels, 'userData':userData, 'allData':allData} #Passing data to HTML template 
    return render(request, 'booking/dashboard.html', context) #DONT FORGET TO ADD CONTEXT AS ARGUMENT

def home(request):
    attendents = attendees.objects.all()
    courses = Course.objects.all()
    TEC_courses = Course.objects.filter(division_access="TEC")
    OPE_courses = Course.objects.filter(division_access="OPE")
    FIN_courses = Course.objects.filter(division_access="FIN")
    MAR_courses = Course.objects.filter(division_access="MAR")
    GLO_courses = Course.objects.filter(division_access="GLO")
    context = {'attendees' : attendents, 'course': courses, 'TEC_courses':TEC_courses, 'OPE_courses':OPE_courses, 'FIN_courses':FIN_courses, 'MAR_courses':MAR_courses, 'GLO_courses':GLO_courses}
    search_input = request.GET.get('search-area') or '' #Getting the value of the searchbar from HTML template
    if search_input: #If there is a value in there
        context['course'] = context['course'].filter(courseName__icontains=search_input) #Creating a queryset which filters the course object so if it contains the value in search bar it will appear, that is icontains
    return render(request, 'booking/home.html', context)

class courses(DetailView): #Using Django generic detail view, this handles lots of things, allows user to see details about a model eg. course
    model = Course
    template_name = 'booking/courses.html'

    def get_queryset(self):
        return Course.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(courses, self).get_context_data(**kwargs)
        context['attendees'] = attendees.objects.filter(course = self.object) #Getting a list of attendees that are related to the course instance
        return context

class book(View): #Creating my own view to have better control over what is happening
    def get(self, request, *args, **kwargs): #This function specifies what happens when the page is loaded
        course_id = self.kwargs.get('pk', None) #Getting the course ID from the URL, the number in URL is called pk
        course = Course.objects.filter(id = course_id) #Creating a queryset and filtering it by the ID got above
        form = bookCourse() #Loading the custom form from forms.py
        attendents = attendees.objects.filter(id = course_id) #Getting list of attendees thatare on the course
        context = {'course': course, 'attendees':attendents, 'form':form}
        return render(request, 'booking/book.html', context)
    
    def post(self, request, *args, **kwargs): #This function specifies what happens when a POST request is sent 
        course_id = self.kwargs.get('pk', None)
        course_inst = Course.objects.get(id = course_id) 
        form = bookCourse(request.POST) #Adding ewquest.POST to capture data sent in the post request
        if form.is_valid():
            data = form.cleaned_data #Getting form data
        if Course.objects.filter(id = course_id).filter(attendees__user=self.request.user).exists(): #Checking to see if the user booking a place has already booked onto that course, doing this by making a queryset to filter the attendees to the current user and if they exist return error
            return HttpResponse('error')
        else:
            attendants = attendees.objects.create(  #Creating an attendants object to be put in database
                user = self.request.user,
                role = data['role'],
                course = course_inst,
                course_due = data['course_due'],
                your_development = data['your_development'],
                )
            email = self.request.user.profile.manager.email #Getting the users manager's email
            url = reverse_lazy('approve', kwargs={'pk':attendants.id}) #Getting the URL for managers to confirm booking place

            send_mail(
                'This is an automatic message', #Subject
                f'Hello {self.request.user.profile.manager}, {self.request.user} has booked onto {course_inst}. Could you please approve or deny their training? To approve please follow this link http://127.0.0.1:8000{url}. ', #Message
                'ilearn112@gmail.com', #From email
                [email], #To email
                
            )
            attendants.save() #DONT FORGET TO SAVE THE OBJECT
            return redirect('home')
    
class viewCourse(View):
    def get(self, request, *args, **kwargs):
        course_id = self.kwargs.get('pk', None)#Getting the course ID from the URL 
        course = Course.objects.filter(id = course_id)#Getting the object that matches that ID
        context = {'course': course}
        return render(request, 'booking/viewCourse.html', context)

class addCourse(CreateView): #Using Django's generic create view, again this handles a lot of things by default like GET & POST functions
    model = Course
    template_name = 'booking/addCourse.html'
    form_class = addCourseForm #Specifying the form to be used from forms.py
    success_url = reverse_lazy('home')

class addProgram(CreateView):
    model = Programs
    template_name = 'booking/addProgram.html'
    form_class = addprogramForm
    success_url = reverse_lazy('home')

class approveBooking(View):
    def get(self, request, *args, **kwargs):
        attend_id = self.kwargs.get('pk', None)
        booking_inst = attendees.objects.get(id = attend_id)
        context = {'bookingInst':booking_inst}
        return render(request,'booking/approveRequest.html', context)
    
    def post(self, request, *args, **kwargs):
        attend_id = self.kwargs.get('pk', None)
        booking_inst = attendees.objects.get(id = attend_id)
        booking_inst.status='APR'
        booking_inst.save()
        return redirect('dashboard')

class deleteBooking(DeleteView): #SImular to create view the delete view can delete objects from database 
    model = attendees
    template_name = "booking/deleteBooking.html"
    context_object_name = 'attendees'
    success_url = reverse_lazy('home')

class completeCourse(View):
    def get(self, request, *args, **kwargs):
        course_id = self.kwargs.get('pk', None) #Get the course ID from URL
        course_inst = Course.objects.get(id = course_id) #Get the individual course by fileting query with the ID
        course_inst.course_completed=True #Mark the course_completed field as true
        course_inst.save() #Save it
        return render(request, 'booking/complete.html')

def insights(request):
    return render(request, 'booking/insights.html')

class rejectBooking(View):
    def get(self, request, *args, **kwargs):
        attend_id = self.kwargs.get('pk', None)
        booking_inst = attendees.objects.get(id = attend_id)
        context = {'bookingInst':booking_inst}
        return render(request,'booking/rejectBooking.html', context)
    
    def post(self, request, *args, **kwargs):
        attend_id = self.kwargs.get('pk', None)
        booking_inst = attendees.objects.get(id = attend_id)
        booking_inst.status='REJ'
        booking_inst.save()
        return redirect('dashboard')

