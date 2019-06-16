from django.shortcuts import render
from django.views.generic import View
from .models import *

# Create your views here.

class ProjectsList(View):
    def get(self,request):
        try:
            us = User.objects.get(username=request.user)
        except:
            us = None
        projects = Project.objects.filter(user=us)
        return render(request,'taskmain/projects_list.html',{'projects':projects,'us':us})

class ProjectDetail(View):
    def get(self,request,slug):
        project = Project.objects.get(slug=slug)
        return render(request,'taskmain/project_detail.html',{'project':project})
