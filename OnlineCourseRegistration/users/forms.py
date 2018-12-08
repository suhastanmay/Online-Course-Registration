from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
	is_student = forms.BooleanField(required=False)
	is_teacher = forms.BooleanField(required=False)

	class Meta(UserCreationForm.Meta):
		model = CustomUser
		fields = ('username', 'email','is_student','is_teacher')

class CustomUserChangeForm(UserChangeForm):
	is_student = forms.BooleanField(required=False)
	is_teacher = forms.BooleanField(required=False)
	class Meta:
		model = CustomUser
		fields = ('username', 'email','is_student','is_teacher')