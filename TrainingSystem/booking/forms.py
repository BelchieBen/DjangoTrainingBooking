from django.db.models import fields
from django import forms
from django.forms import widgets
from .models import Course, Programs, attendees

staff=[
        ('CAL', 'CALUM'),
        ('YAN', 'YANNA'),
        ('HAN', 'HANNA'),
        ('EXT', 'EXTERNAL'),
]
class addCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
   
    courseName = forms.CharField(required=True)
    courseDesc = forms.CharField(required=True, widget=forms.Textarea)
    host = forms.ChoiceField(choices=staff, required=True)
    min_participants = forms.IntegerField(required=True)
    max_participants = forms.IntegerField(required=True)
    start_date = forms.DateTimeField(required=True, input_formats=[ '%d/%m/%Y %H:%M'])
    end_date = forms.DateTimeField(required=True, input_formats=[ '%d/%m/%Y %H:%M'])

class addprogramForm(forms.ModelForm):
    class Meta:
        model = Programs
        fields = '__all__'

class bookCourse(forms.ModelForm):
    class Meta:
        model = attendees
        fields = ['manager', 'role', 'department', 'course_due', 'your_development']
        labels = {
            'your_development':'How has this training been identified? How will you apply the learning in your role? How will you measure the success of this learning?',
            'role':'Your Job Title'
        }
        widgets = {
            'your_development': widgets.Textarea()
        }

    
    