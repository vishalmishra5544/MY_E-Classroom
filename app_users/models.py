from django.db import models
from django.contrib.auth.models import User
import os
# from django.utils import timezone
from django.urls import reverse
from curriculum.models import Standard,Subject,Lesson
from django.contrib.auth.models import AbstractUser


def path_and_rename(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.pk, ext)
    return os.path.join(upload_to, filename)

class UserProfileInfo(models.Model):

    #creating a relationship with user class (not inheriting)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #adding additional attributes
    bio = models.CharField(max_length=500)
    profile_pic = models.ImageField(upload_to=path_and_rename, verbose_name="Profile Picture", blank=True)
    teacher = 'teacher'
    student = 'student'
    parent = 'parent'
    user_types = [
        (teacher, 'teacher'),
        (student, 'student'),
        (parent, 'parent'),
    ]
    user_type = models.CharField(max_length=10, choices=user_types,default=student)

    def __str__(self):
        return self.user.username

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    feedback = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')


class StudentAttendance(models.Model):
    roll_no = models.CharField(max_length=100)
    studentname = models.CharField(max_length=100)
    standard = models.CharField(max_length=100,default=12,null=True,blank=True)
    subject = models.CharField(max_length=100,default='English',null=True,blank=True)
    #standard = models.ForeignKey(Standard,on_delete=models.CASCADE,null=True,blank=True)
    #subject = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True,blank=True)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    status = models.CharField(max_length=100,default='Absent')
    def __str__(self):
        return self.studentname


class Applications(models.Model):
    roll_no = models.CharField(max_length=100)
    studentname = models.CharField(max_length=100)
    standard = models.CharField(max_length=100, default=12, null=True, blank=True)
    date = models.CharField(max_length=100)
    applicationtype = models.CharField(max_length=100)
    applicationdetail = models.CharField(max_length=100)
    applicationstatus = models.CharField(max_length=100,default='unaccepted')

    def __str__(self):
        return self.applicationtype

class Question(models.Model):
    course=models.ForeignKey(Standard,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField()
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)

class Result(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    exam = models.ForeignKey(Standard,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

