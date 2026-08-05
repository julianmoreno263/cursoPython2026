
from django.shortcuts import render,HttpResponse
from .models import Project

# Create your views here.
def profile(request):
    # p1=Project(title='Curso de html', desc='descripcion de html')
    # p1.save()
    # p2=Project(title='Curso de css', desc='descripcion de css')
    # p2.save()
    # p3=Project(title='Curso de django', desc='descripcion de django')
    # p3.save()

    projects=Project.objects.all()
    print(projects)

    return HttpResponse(projects)