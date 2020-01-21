from django.shortcuts import render
from projects.models import Project

from projects.models import Project
from projects.serializers import ProjectSerializer
from rest_framework import generics

def project_index(request):
	projects = Project.objects.all()
	context = {
		'projects': projects
	}
	return render(request, 'project_index.html', context)

def project_detail(request, pk):
	project = Project.objects.get(pk=pk)
	context = {
		'project': project
	}
	return render(request, 'project_detail.html', context)




class ProjectListCreate(generics.ListCreateAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer