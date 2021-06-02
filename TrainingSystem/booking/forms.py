from django.db.models import fields
from django import forms
from .models import Course

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