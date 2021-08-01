from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class UserRegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class ReportForm(forms.ModelForm):
	class Meta:
		model = Report
		fields = ['title','body', 'supervisor']


class ProcessReportForm(forms.ModelForm):
	class Meta:
		model = ProcessReport
		fields = ['status', 'additional_information', 'report']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image', 'project_title', 'project_details']


# class ProjectStatusForm(forms.ModelForm):
# 	class Meta:
# 		model = ProjectStatus
# 		fields = ['profile', 'status']