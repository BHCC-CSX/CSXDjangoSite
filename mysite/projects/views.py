from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError
from rest_framework import generics

from .models import Project
from .forms import ProposalForm
from .serializers import ProjectSerializer


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


def project_proposal(request):
    form = ProposalForm(request.POST, request.FILES)
    if form.is_valid():
        form.process_proposal()
        try:
            send_mail('Alert: Project proposal submitted', 'For more info visit https://www.bhcc-csx.appspot.com/admin/',
                      'cjsuth1@gmail.com', ['cjsuth1@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

        return HttpResponseRedirect(reverse('project_proposal_confirm'))

    return render(request, "project_proposal.html", {'form': form})


def project_proposal_confirm(request):
    return render(request, "project_proposal_confirm.html")


class ProjectListCreate(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
