from datetime import date
from dateutil.relativedelta import *
from django.core.mail import send_mail
from booking.models import Course

def run():
    for course in Course.objects.filter(start_date = date.today() + relativedelta(days=1)):
       for attendant in course.attendees_set():
           print(attendant.email)
           send_mail(
               'Course Reminder', #Subject
                f'Hello {attendant}, Dont forget that you have a training course {course} tomorrow!',
                'ilearn112@gmail.com',#From email
                [attendant.email],#To email
           ) 

# Need to make this run daily / every so often

