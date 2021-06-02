from django.shortcuts import render
from .models import attendees, Course
from django.views.generic.detail import DetailView


def dashboard(request):
    attendents = attendees.objects.all()
    courses = Course.objects.all()
    context = {'attendees' : attendents, 'course': courses}
    return render(request, 'booking/dashboard.html', context)

def home(request):
    attendents = attendees.objects.all()
    courses = Course.objects.all()
    context = {'attendees' : attendents, 'course': courses}
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

