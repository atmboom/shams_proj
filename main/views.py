from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.http import JsonResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from .forms import *
from .decorators import allowed_users

# Create your views here.
@login_required
@allowed_users(allowed=["Student"])
def home(request):
	reports = Report.objects.filter(student=request.user).all()
	processed_reports = ProcessReport.objects.filter(report__student=request.user).all()
	context = {"reports":reports, 
	"processed_reports":processed_reports
	}
	return render(request, 'main/home.html', context)

@login_required
def projects(request):
	projects = ProjectStatus.objects.filter(complete="Yes")
	context = {"projects":projects}
	return render(request, 'main/complete_projects.html', context)

@login_required
@allowed_users(allowed=["Student"])
def suggested_projects(request):
	projects = SuggesstedProjects.objects.all().order_by('-date')
	context={"projects":projects}
	return render(request, 'main/suggested_projs.html', context)

@login_required
@allowed_users(allowed=["Supervisor"])
def S_suggested_projects(request):
	projects = SuggesstedProjects.objects.all().order_by('-date')
	context={"projects":projects}
	return render(request, 'main/S_suggested_projs.html', context)

class CreateSuggesstedProjects(LoginRequiredMixin, CreateView):
	model = SuggesstedProjects
	template_name = 'main/suggest_proj.html'
	fields = ['name']
	redirect_url = 'S_suggessted_projects'

	def form_valid(self, form):
		form.instance.supervisor = self.request.user.supervisor
		return super().form_valid(form)

def after_login(request):
    if is_student(request.user):      
        return redirect('home')           
    elif is_supervisor(request.user):
        return redirect('lecturer')
    elif is_admin(request.user):
    	return redirect('project_list')
    else:
        return redirect('login')

def is_student(user):
    return user.groups.filter(name='Student').exists()

def is_supervisor(user):
    return user.groups.filter(name='Supervisor').exists()

def is_admin(user):
	return user.groups.filter(name="Admin").exists()

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			group = Group.objects.get(name='Student')
			user.groups.add(group)
			return redirect('login')
	else:
		form = UserRegisterForm()		
	return render(request, 'main/register.html', {'form':form})

@login_required
@allowed_users(allowed=["Supervisor"])
def lecturer(request):
	reports = Report.objects.filter(supervisor=request.user.supervisor).all()
	processed_reports = ProcessReport.objects.filter(supervisor=request.user.supervisor).all()
	context = {"reports":reports, "processed_reports":processed_reports}
	return render(request, 'main/lecturer.html', context)

@login_required
@allowed_users(allowed=["Admin"])
def project_list(request):
	profile = ProjectStatus.objects.all()
	context = {'profiles':profile}
	return render(request, 'main/project_list.html', context)


class ProjectUpdate(LoginRequiredMixin, UpdateView):
	model = ProjectStatus
	fields = ['profile', 'status', 'complete']
	success_url = "/"


@login_required 
@allowed_users(allowed=["Student"])
def profile(request):
		profile_form = ProfileUpdateForm()
		if request.method=='POST':
			profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if profile_form.is_valid():
			profile_form.save()
			return redirect('profile')
		else:
			profile_form = ProfileUpdateForm(instance=request.user.profile)
		context = {
        	'profile_form':profile_form,
    	}
		return render(request, 'main/profile.html', context)


class CreateReport(LoginRequiredMixin, CreateView):
	model = Report
	fields = ['title', 'file', 'supervisor']
	template_name = 'main/create_report.html'
	success_url = '/'

	def form_valid(self, form):
		form.instance.student = self.request.user
		return super().form_valid(form)


class ReportDetail(DetailView):
	model = Report
	context_object_name = 'report'
	template_name = 'main/report_detail.html'


class LecturerReportDetail(DetailView):
	model = Report
	context_object_name = 'report'
	template_name = 'main/lecturer_report_detail.html'


class ReportUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Report
	context_object_name = 'reports'
	fields = ['title', 'file', 'supervisor']
	template_name = 'main/update_report.html'
	success_url = '/'

	def test_func(self):
		report = self.get_object()
		if self.request.user == report.student:
			return True
		return False

class ReportProcess(LoginRequiredMixin, UpdateView):
	model = Report
	context_object_name = 'reports'
	fields = ['title', 'status', 'supervisor_remarks']
	template_name = 'main/report_process.html'
	success_url = '/'
