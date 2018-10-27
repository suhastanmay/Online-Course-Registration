from django.urls import path,include
from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views
from  .views import CourseListView



app_name = 'users'


app_name = 'users'
urlpatterns = [
	path('signup/', views.SignUp.as_view(), name='signup'),
	path('', views.index, name='index'),
	path('<int:course_id>/', views.details, name='details'),
	path('add_course/', views.add_course, name='add_course'),
	path('add_student/', views.add_student, name='add_student'),
	path('audit_course/', views.audit_course, name='audit_course'),
	path('<int:course_id>/add_course_details/', views.add_course_details, name='add_course_details'),
	path('add_grade/',views.add_grade,name='add_grade'),
	path('publish_course_registration/',views.publish_course_registration, name='publish_course_registration'),
	path('view_registration/',views.view_registration, name='view_registration'),
	path('faculty/', views.faculty, name='faculty'),
	path('<int:course_id>/add_course_details/', views.add_course_details, name='add_course_details'),
	path('Students.html/', CourseListView.as_view(),name='MyCourseList'),
]
