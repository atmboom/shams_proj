"""underGrad_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import (home, CreateReport, ReportDetail, ReportUpdate, register, 
    lecturer, 
    # CreateProcessReport,
     profile, project_list, ProjectUpdate, after_login, ReportProcess, suggested_projects,S_suggested_projects,
    LecturerReportDetail, projects, CreateSuggesstedProjects)
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name="home"),
    path('', after_login, name="after_login"),
    path('register/', register, name="register"),
    path('projects/', projects, name="projects"),
    path('suggest_project/', CreateSuggesstedProjects.as_view(), name="suggest_project"),
    path('S_suggested_projects/', S_suggested_projects, name="S_suggested_projects"),
    path('suggested_projects/', suggested_projects, name="suggested_projects"),
    path('create_report/', CreateReport.as_view(), name="create_report"),
    # path('process_report/', CreateProcessReport.as_view(), name="process_report"),
    path('update_report/<int:pk>/', ReportUpdate.as_view(), name="update_report"),
    path('report_process/<int:pk>/', ReportProcess.as_view(), name="report_process"),
    path('report_detail/<int:pk>/', ReportDetail.as_view(), name="report_detail"),
    path('detail_report/<int:pk>/', LecturerReportDetail.as_view(), name="detail_report"),
    path('lecturer/', lecturer, name="lecturer"),
    path('profile/', profile, name='profile'),
    path('project_list/', project_list, name='project_list'),
    path('update_project_title/<int:pk>/', ProjectUpdate.as_view(template_name="main/update_project_title.html"), name="update_project_title"),
    path('login/', LoginView.as_view(template_name='main/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='main/logout.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
