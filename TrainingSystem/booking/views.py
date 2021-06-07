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

def dashboard(request):
    attendents = attendees.objects.all()
    courses = Course.objects.all()
    programs = Programs.objects.all()
    emptDict = {}
    for event in courses:
        attendies =  event.attendees_set.filter(approved=True).count()
        emptDict[event.courseName] = attendies

    valueList = []
    labels = []
    for key,value in emptDict.items():
        valueList.append(value)
        labels.append(str(key))

    context = {'attendees' : attendents, 'course': courses, 'programs': programs, 'attendants':emptDict, 'valueList':valueList, 'labels':labels}
    return render(request, 'booking/dashboard.html', context)

def home(request):
    attendents = attendees.objects.all()
    courses = Course.objects.all()
    context = {'attendees' : attendents, 'course': courses}
    search_input = request.GET.get('search-area') or ''
    if search_input:
        context['course'] = context['course'].filter(courseName__icontains=search_input)
    return render(request, 'booking/home.html', context)

class courses(DetailView):
    model = Course
    template_name = 'booking/courses.html'

    def get_queryset(self):
        return Course.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(courses, self).get_context_data(**kwargs)
        context['attendees'] = attendees.objects.filter(course = self.object)
        return context

class book(View):
    def get(self, request, *args, **kwargs):
        course_id = self.kwargs.get('pk', None)
        course = Course.objects.filter(id = course_id)
        form = bookCourse()
        attendents = attendees.objects.filter(id = course_id)
        context = {'course': course, 'attendees':attendents, 'form':form}
        return render(request, 'booking/book.html', context)
    
    def post(self, request, *args, **kwargs):
        course_id = self.kwargs.get('pk', None)
        course_inst = Course.objects.get(id = course_id) 
        form = bookCourse(request.POST)
        if form.is_valid():
            data = form.cleaned_data
        if Course.objects.filter(id = course_id).filter(attendees__user=self.request.user).exists():
            return HttpResponse('error')
        else:
            attendants = attendees.objects.create(
                user = self.request.user,
                manager = data['manager'],
                role = data['role'],
                department = data['department'],
                course = course_inst,
                course_due = data['course_due'],
                your_development = data['your_development'],
                )
            email = self.request.user.profile.manager.email
            url = reverse_lazy('approve', kwargs={'pk':attendants.id})

            send_mail(
                'This is an automatic message',
                f'Hello {self.request.user.profile.manager}, {self.request.user} has booked onto {course_inst}. Could you please approve or deny their training? To approve please follow this link http://127.0.0.1:8000{url}. ',
                'ilearn112@gmail.com',
                [email],
                
            )
            attendants.save()
            return redirect('home')
    
class viewCourse(View):
    def get(self, request, *args, **kwargs):
        course_id = self.kwargs.get('pk', None)#Getting the course ID from the URL 
        course = Course.objects.filter(id = course_id)#Getting the object that matches that ID
        context = {'course': course}
        return render(request, 'booking/viewCourse.html', context)

class addCourse(CreateView):
    model = Course
    template_name = 'booking/addCourse.html'
    form_class = addCourseForm
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
        booking_inst.approved=True
        booking_inst.save()
        return HttpResponse('Success')

class deleteBooking(DeleteView):
    model = attendees
    template_name = "booking/deleteBooking.html"
    context_object_name = 'attendees'
    success_url = reverse_lazy('home')

class completeCourse(View):
    def get(self, request, *args, **kwargs):
        course_id = self.kwargs.get('pk', None)
        course_inst = Course.objects.get(id = course_id) 
        course_inst.course_completed=True
        course_inst.save()
        return render(request, 'booking/complete.html')

