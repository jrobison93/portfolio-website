from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

from .models import Project

def index(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {'project_list': projects})

# Create your views here.
def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/detail.html', {'project' : project})
