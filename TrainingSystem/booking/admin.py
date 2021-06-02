from django.contrib import admin
from .models import Course, attendees

admin.site.register(Course)
admin.site.register(attendees)
