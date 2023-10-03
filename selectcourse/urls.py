from django.urls import path
from . import views

app_name='selectcourse'

urlpatterns=[
    path('term/<int:termid1>', views.GetTerm),
    path('course/list/<int:termid1>', views.LoadCourse),
    path('term', views.TermList),
    path('term/create',views.CreateTerm),
    path('term/update/<int:tid>', views.EditTerm),
    path('term/del/<int:tid>',views.delTerm),
    path('course',views.CourseList, name="course"),
    path('course/create',views.CreateCourse),
    path('course/update/<int:cid>', views.EditCourse),
    path('course/del/<int:cid>', views.delCourse),
    path('selectcourse',views.SelectCourseList, name='selcourse'),
    path('selectcourse/update/<int:scid1>', views.EditSelectCourse),
    path('selectcourse/del/<int:scid1>', views.delSelectCourse),
    path('selectcourse/create', views.CreateSelectCourse)
]