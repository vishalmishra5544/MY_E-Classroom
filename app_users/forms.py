from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_users.models import UserProfileInfo,StudentAttendance,Applications,Question
from curriculum.models import Standard

class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ('username','first_name','last_name', 'email', 'password1', 'password2')

        # widgets = {
        # "password":"forms.PasswordInput()",
        # }

        labels = {
        'password1':'Password',
        'password2':'Confirm Password'
        }

class UserProfileInfoForm(forms.ModelForm):
    bio = forms.CharField(required=False)
    teacher = 'teacher'
    student = 'student'
    parent = 'parent'
    user_types = [
        (student, 'student'),
    ]
    user_type = forms.ChoiceField(required=True, choices=user_types)

    class Meta():
        model = UserProfileInfo
        fields = ('bio', 'profile_pic', 'user_type')

class StudAttendanceForm(forms.ModelForm):
    class Meta:
        model = StudentAttendance
        fields = ['roll_no','studentname','standard','subject','date','time','status']
        widgets = {
            'roll_no':forms.TextInput(attrs={'class':'form-control'}),
            'studentname': forms.TextInput(attrs={'class': 'form-control'}),
            'standard': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control'}),
            'time': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Applications
        fields = ['roll_no','studentname','standard','date','applicationtype','applicationdetail','applicationstatus']
        widgets = {
            'roll_no':forms.TextInput(attrs={'class':'form-control'}),
            'studentname': forms.TextInput(attrs={'class': 'form-control'}),
            'standard': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control'}),
            'applicationtype': forms.TextInput(attrs={'class': 'form-control'}),
            'applicationdetail': forms.TextInput(attrs={'class': 'form-control'}),
            'applicationstatus': forms.TextInput(attrs={'class': 'form-control'}),
        }


class QuestionForm(forms.ModelForm):
    # this will show dropdown __str__ method course model is shown on html so override it
    # to_field_name this will fetch corresponding value  user_id present in course model and return it
    courseID = forms.ModelChoiceField(queryset=Standard.objects.all(), empty_label="Course Name",
                                      to_field_name="id")

    class Meta:
        model = Question
        fields = ['marks', 'question', 'option1', 'option2', 'option3', 'option4', 'answer']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3, 'cols': 50})
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Standard
        fields = ['name','question_number','total_marks']