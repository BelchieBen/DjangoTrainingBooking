from django import forms

staff=(
        ('CAL', 'CALUM'),
        ('YAN', 'YANNA'),
        ('HAN', 'HANNA'),
        ('EXT', 'EXTERNAL'),
    )

class addCourseForm(forms.Form):
    courseName = forms.CharField(required=True)
    courseDesc = forms.CharField(required=True, widget=forms.Textarea)
    host = forms.MultipleChoiceField(choices=staff, widget=forms.CheckboxSelectMultiple, required=True)
    min_participants = forms.IntegerField(required=True)
    max_participants = forms.IntegerField(required=True)
    start_date = forms.DateTimeField(required=True, input_formats=[ '%m/%d/%y %H:%M:%S'])
    end_date = forms.DateTimeField(required=True, input_formats=[ '%m/%d/%y %H:%M:%S'])