from django.urls import path
from .import views
from django.shortcuts import HttpResponseRedirect

app_name='rollcallmodule'

urlpatterns=[
    path('coursepopup', views.CoursePopUp),
    path('coursepopup/ok', views.CoursePopUpOk),
    path('ExtractingComparing', views.ExtractingComparingPage),
    path('MyAttendance', views.MyAttendancePage),
    path('RollCallPage', views.RollCallPage),
    path('RollCallPage/update/<int:sid>', views.EditRollCallPage),
    path('RollCallPage/delete/<int:sid>', views.DelRollCallPage),
    path('StudentInformation', views.ViewStudentInformation),
    path('UploadClassStudentPhoto', views.UploadClassStudentPhoto),
    path('UploadClassStudentPhoto/upload', views.upload),
    path('UploadClassStudentPhoto/reset', views.Udelete),
    path('UploadClassStudentPhoto/proceed', views.Attendancerun),
    path('StudentInformation/importstu',views.importstu),
    path('history',views.HistoryRec),
    path('history/update/<int:aid>', views.EditHistory)
]