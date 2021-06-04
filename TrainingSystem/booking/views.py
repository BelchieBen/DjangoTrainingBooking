from django.shortcuts import render, redirect
from .models import attendees, Course
from django.views.generic.detail import DetailView
from django.views.generic import View, CreateView
from .forms import addCourseForm
from django.urls import reverse, reverse_lazy


def dashboard(request):
    attendents = attendees.objects.all()
    courses = Course.objects.all()
    c = Course.objects.get(id=1)
    att = c.attendents_set.all()
    print(att)
    context = {'attendees' : attendents, 'course': courses}
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
        context = {'course': course}
        return render(request, 'booking/book.html', context)
    
    def post(self, request, *args, **kwargs):
        course_id = self.kwargs.get('pk', None)
        course_inst = Course.objects.get(id = course_id)
        attendants = attendees.objects.create(user = self.request.user, course = course_inst)
        attendants.save()
        return redirect('home')

class addCourse(CreateView):
    model = Course
    template_name = 'booking/addCourse.html'
    form_class = addCourseForm
    success_url = reverse_lazy('home')
