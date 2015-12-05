from django.shortcuts import render
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
import os

def index(request):
    return render(request, 'portfolio/index.html', )


def resume(request):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    resume_path = current_dir + '\\static\\portfolio\\pdfs\\resume.pdf'

    image_data = open(resume_path, "rb").read()
    return HttpResponse(image_data, content_type='application/pdf')
