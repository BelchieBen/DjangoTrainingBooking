from django.conf import settings
from booking.models import Course
from datetime import datetime, timedelta
from django.core.mail import send_mail

def test():
    print("This means it is working!")

def remind_participants():
    today = datetime.utcnow().date()
    tomorrow = today + timedelta(days=1)
    course = Course.objects.filter(course_completed=False)
    for c in course:
        if c.start_date.date() == tomorrow:
            attendees = c.attendees_set.all().values_list('user__email', flat=True)
            print(attendees)
            send_mail(
                "This is a course reminder",
                f"Hello, this is a automatic reminder that you are booked onto the course {c.courseName} tomorrow. Dont forget!",
                "ilearn112@gmail.com",
                attendees,
            )
            
            print("There is a course for tomorrow! It is "+str(c.courseName) )