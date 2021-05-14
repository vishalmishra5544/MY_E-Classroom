from django.contrib import admin
from app_users.models import UserProfileInfo, StudentAttendance , Applications ,Question ,Result
# Register your models here.
admin.site.register(UserProfileInfo)
""""@admin.register(StudentAttendance)"""
class StudAdmin(admin.ModelAdmin):
    list_display = ('id','roll_no','studentname','standard','subject','date','time','status')
admin.site.register(StudentAttendance,StudAdmin)

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id','roll_no','studentname','standard','date','applicationtype','applicationdetail','applicationstatus')
admin.site.register(Applications,ApplicationAdmin)

admin.site.register(Question)
admin.site.register(Result)