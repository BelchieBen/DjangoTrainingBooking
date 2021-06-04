from django.contrib import admin
from .models import Course, attendees, Programs

admin.site.register(Course)
admin.site.register(attendees)
admin.site.register(Programs)
