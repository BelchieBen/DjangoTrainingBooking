from datetime import datetime, timedelta
from workers import task
from django.core.mail import send_mail
from booking.models import Course, attendees

course_reminder = datetime.utcnow() + timedelta(days=1)

@task()
def test():
    print("Hello users")

test()


# @task()
# def trial_ending():
#     print("Hellooo")
#     for attendants in attendees.objects.filter(course__start_date=datetime.utcnow()+timedelta(days=1)):
#         send_mail(
#             'This is a reminder message',
#             f'Hello {attendants.user}, This is a reminder that you are booked onto {attendants}! ',
#             'ilearn112@gmail.com',
#             ['belchieben112@gmail.com'],
#         )
#         print(attendants)
#         print(attendants.user.email)
    
# trial_ending()