from django.urls import path
from app_users import views


# app_name = 'app_users'
urlpatterns = [
    path('',views.HomeView.as_view(),name='index'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('Dashboard/', views.dashboard, name='dashboard'),
    path('Dashboard/applications/', views.applications, name='applications'),
    path('Dashboard/applications/<int:id>/', views.updateapplication, name='updateapplication'),
    path('Dashboard/applications/delete/<int:id>/', views.deleteapplication, name='deleteapplication'),
    path('Dashboard/attendance/', views.attendance, name='attendance'),
    path('Dashboard/attendance/submitattendance/', views.submitattendance, name='submitattendance'),
    path('Dashboard/attendance/viewattendance/', views.viewattendance, name='viewattendance'),
    path('Dashboard/attendance/takeattendance/', views.takeattendance, name='takeattendance'),
    path('Dashboard/attendance/takeattendance/<int:id>/', views.update_data, name='update_data'),
    path('Dashboard/attendance/takeattendance/delete/<int:id>/', views.delete_data, name='delete_data'),
    # path('Dashboard/attendance/viewattendance', views.viewattendance, name='viewattendance'),
    path('Dashboard/assignments/', views.assignments, name='assignments'),
    path('Dashboard/assignments/teacher_exam/', views.teacher_exam_view, name='teacher_exam'),
    path('Dashboard/assignment/teacher_exam/teacher_add_exam/', views.teacher_add_exam_view, name='teacher_add_exam'),
    path('Dashboard/assignments/teacher_exam/teacher_view_exam/', views.teacher_view_exam_view, name='teacher_view_exam'),
    path('Dashboard/assignments/teacher_exam/teacher_view_exam/delete_exam_view/<int:pk>', views.delete_exam_view, name='delete_exam_view'),
    path('Dashboard/assignments/teacher_question/', views.teacher_question_view, name='teacher_question'),
    path('Dashboard/assignments/teacher_question/teacher_add_question/', views.teacher_add_question_view, name='teacher_add_question'),
    path('Dashboard/assignments/teacher_question/teacher_view_question/', views.teacher_view_question_view, name='teacher_view_question'),
    path('Dashboard/assignments/teacher_question/teacher_view_question/see_question/<int:pk>/', views.see_question_view,name='see_question'),
    path('Dashboard/assignments/teacher_question/teacher_view_question/remove-question/<int:pk>/', views.remove_question_view,name='remove_question'),
    path('Dashboard/assignments/student_dashboard/', views.student_dashboard_view, name='student_dashboard'),
    path('Dashboard/assignments/student_dashboard/student_exam/', views.student_exam_view,name='student_exam'),
    path('Dashboard/assignments/student_dashboard/student_exam/take-exam/<int:pk>/', views.take_exam_view,name='take_exam'),
    path('Dashboard/assignments/student_dashboard/student_exam/take-exam/start-exam/<int:pk>/', views.start_exam_view,name='start_exam'),
    path('Dashboard/assignments/student_dashboard/student_exam/take-exam/start-exam/calculate-marks/', views.calculate_marks_view,name='calculate_marks'),
    path('view-result/', views.view_result_view,name='view_result'),
    path('check-marks/<int:pk>/', views.check_marks_view,name='check_marks'),
    path('student-marks/', views.student_marks_view,name='student_marks'),

]
