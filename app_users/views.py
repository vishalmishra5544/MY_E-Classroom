from django.shortcuts import render
from app_users.forms import UserForm, UserProfileInfoForm , StudAttendanceForm ,ApplicationForm, QuestionForm , CourseForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from curriculum.models import Standard
from .models import UserProfileInfo, Contact, StudentAttendance , Applications ,Question ,Result
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.core.paginator import Paginator

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT IS DEACTIVATED")
        else:
            return HttpResponse("Please use correct id and password")
            # return HttpResponseRedirect(reverse('register'))

    else:
        return render(request, 'app_users/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


# Create your views here.
# def index(request):
#     return render(request,'app_users/index.html')

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'app_users/registration.html',
                            {'registered':registered,
                             'user_form':user_form,
                             'profile_form':profile_form})

class HomeView(TemplateView):
    template_name = 'app_users/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        standards = Standard.objects.all()
        teachers = UserProfileInfo.objects.filter(user_type='teacher')
        context['standards'] = standards
        context['teachers'] = teachers
        return context

class ContactView(CreateView):
    model = Contact
    fields = '__all__'
    template_name = 'app_users/contact.html'


def aboutus(request):
    return render(request,'app_users/aboutus.html')

def dashboard(request):
    teacher = True
    student = True
    admin = True
    return render(request,'app_users/dashboard.html')
def attendance(request):
    return render(request,'app_users/attendance.html')
def takeattendance(request):
    if request.method == 'POST':
        fm = StudAttendanceForm(request.POST)
        if fm.is_valid():
            fm.save()
        fm = StudAttendanceForm(request.POST)
    else:
        fm = StudAttendanceForm()
    stud =StudentAttendance.objects.all()
    return render(request,'app_users/take_attendance.html',{'form':fm,'stu':stud})
def delete_data(request,id):
    if request.method=='POST':
        pi = StudentAttendance.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect(reverse('takeattendance'))
def update_data(request,id):
    if request.method=='POST':
        pi = StudentAttendance.objects.get(pk=id)
        fm = StudAttendanceForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = StudentAttendance.objects.get(pk=id)
        fm = StudAttendanceForm( instance=pi)
    return render(request,'app_users/updateattendance.html',{'form':fm})
def viewattendance(request):
   if request.method =='POST':
     searched =request.POST['searched']
     posts = StudentAttendance.objects.filter(studentname=searched)
     return render(request,'app_users/view_attendance.html',{'searched':searched,'posts':posts})
   else:
      return render(request,'app_users/view_attendance.html',{})


def submitattendance(request):
    if request.method == 'POST':
        fm = StudAttendanceForm(request.POST)
        if fm.is_valid():
            fm.save()
        fm = StudAttendanceForm(request.POST)
    else:
        fm = StudAttendanceForm()
    return render(request, 'app_users/submit_attendance.html', {'form': fm})

def applications(request):
    if request.method == 'POST':
        fm = ApplicationForm(request.POST)
        if fm.is_valid():
            fm.save()
        fm = ApplicationForm(request.POST)
    else:
        fm = ApplicationForm()
    stud = Applications.objects.all()

    return render(request, 'app_users/applications.html', {'form': fm, 'stu': stud})
def updateapplication(request,id):
    if request.method=='POST':
        pi = Applications.objects.get(pk=id)
        fm = ApplicationForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Applications.objects.get(pk=id)
        fm = ApplicationForm( instance=pi)
    return render(request,'app_users/updateapplication.html',{'form':fm})

def deleteapplication(request,id):
    if request.method=='POST':
        pi = Applications.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect(reverse('applications'))



def assignments(request):
    return render(request, 'app_users/assignments.html')
@login_required # (login_url='adminlogin')
def view_question_view(request,pk):
    questions = Question.objects.all().filter(course_id=pk)
    return render(request,'app_users/quiz/view_question.html',{'questions':questions})

@login_required # (login_url='adminlogin')
def delete_question_view(request,pk):
    question = Question.objects.get(id=pk)
    question.delete()
    return HttpResponseRedirect('/admin_view_question')


@login_required #(login_url='studentlogin')
def student_dashboard_view(request):
    dict = {

        'total_course': Standard.objects.all().count(),
        'total_question': Question.objects.all().count(),
    }
    return render(request, 'app_users/quiz/student_dashboard.html', context=dict)


@login_required #(login_url='studentlogin')
def student_exam_view(request):
    courses = Standard.objects.all()
    return render(request, 'app_users/quiz/student_exam.html', {'courses': courses})


@login_required # (login_url='studentlogin')
def take_exam_view(request, pk):
    course = Standard.objects.get(id=pk)
    total_questions = Question.objects.all().filter(course=course).count()
    questions = Question.objects.all().filter(course=course)
    total_marks = 0
    for q in questions:
        total_marks = total_marks + q.marks

    return render(request, 'app_users/quiz/take_exam.html',
                  {'course': course, 'total_questions': total_questions, 'total_marks': total_marks})


@login_required #(login_url='studentlogin')
def start_exam_view(request, pk):
    course = Standard.objects.get(id=pk)
    questions = Question.objects.all().filter(course=course)
    if request.method == 'POST':
        pass
    response = render(request, 'app_users/quiz/start_exam.html', {'course': course, 'questions': questions})
    response.set_cookie('course_id', course.id)
    return response


@login_required # (login_url='studentlogin')
def calculate_marks_view(request):
    if request.COOKIES.get('course_id') is not None:
        course_id = request.COOKIES.get('course_id')
        course = Standard.objects.get(id=course_id)

        total_marks = 0
        questions = Question.objects.all().filter(course=course)
        for i in range(len(questions)):

            selected_ans = request.COOKIES.get(str(i + 1))
            actual_answer = questions[i].answer
            if selected_ans == actual_answer:
                total_marks = total_marks + questions[i].marks
        student = User.objects.get(id=request.user.id)
        result = Result()
        result.marks = total_marks
        result.exam = course
        result.student = student
        result.save()

        return HttpResponseRedirect(reverse('view_result'))


@login_required #(login_url='studentlogin')

def view_result_view(request):
    courses = Standard.objects.all()
    return render(request, 'app_users/quiz/view_result.html', {'courses': courses})


@login_required #(login_url='studentlogin')

def check_marks_view(request, pk):
    course = Standard.objects.get(id=pk)
    student = User.objects.get(id=request.user.id)
    results = Result.objects.all().filter(exam=course)
    return render(request, 'app_users/quiz/check_marks.html', {'results': results,'student':student})


@login_required #(login_url='studentlogin')

def student_marks_view(request):
    courses = Standard.objects.all()
    return render(request, 'app_users/quiz/student_marks.html', {'courses': courses})


@login_required #(login_url='teacherlogin')
def teacher_exam_view(request):
    return render(request,'app_users/quiz/teacher_exam.html')

@login_required #(login_url='teacherlogin')
def teacher_add_exam_view(request):
    courseForm = CourseForm()
    if request.method=='POST':
        courseForm = CourseForm(request.POST)
        if courseForm.is_valid():
            courseForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect(reverse('teacher_exam'))
    return render(request,'app_users/quiz/teacher_add_exam.html',{'courseForm':courseForm})

@login_required # (login_url='teacherlogin')
def teacher_view_exam_view(request):
    courses = Standard.objects.all()
    return render(request,'app_users/quiz/teacher_view_exam.html',{'courses':courses})

@login_required # (login_url='teacherlogin')
def delete_exam_view(request,pk):
    course= Standard.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect(reverse('teacher_view_exam'))

@login_required(login_url='adminlogin')
def teacher_question_view(request):
    return render(request,'app_users/quiz/teacher_question.html')

@login_required # (login_url='teacherlogin')
def teacher_add_question_view(request):
    questionForm = QuestionForm()
    if request.method =='POST':
        questionForm = QuestionForm(request.POST)
        if questionForm.is_valid():
            question = questionForm.save(commit=False)
            course = Standard.objects.get(id=request.POST.get('courseID'))
            question.course = course
            question.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect(reverse('teacher_view_question'))
    return render(request,'app_users/quiz/teacher_add_question.html',{'questionForm':questionForm})

@login_required #(login_url='teacherlogin')
def teacher_view_question_view(request):
    courses = Standard.objects.all()
    return render(request,'app_users/quiz/teacher_view_question.html',{'courses':courses})

@login_required #(login_url='teacherlogin')

def see_question_view(request,pk):
    questions = Question.objects.all().filter(course_id=pk)
    return render(request,'app_users/quiz/see_question.html',{'questions':questions})

@login_required #(login_url='teacherlogin')
def remove_question_view(request,pk):
    question = Question.objects.get(id=pk)
    question.delete()
    return HttpResponseRedirect(reverse('teacher_view_question'))

