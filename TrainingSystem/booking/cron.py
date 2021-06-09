from .models import Course
from datetime import datetime, timedelta
def remind_participants():
    today = datetime.utcnow().date()
    tomorrow = today + timedelta(days=1)
    course = Course.objects.filter(course_completed=False)
    for c in course:
        if c.start_date.date() == tomorrow:
            print("There is a course for tomorrow! It is "+str(c.courseName) )

