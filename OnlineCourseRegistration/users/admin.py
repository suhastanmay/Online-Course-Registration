from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from .models import Course,AcademicCourse


from .models import Course, Grade, AuditCourse

# Register your models here.

class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = ['email', 'username',]
	
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(AuditCourse)
admin.site.register(AcademicCourse)
