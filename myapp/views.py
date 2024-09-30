from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project,Task
# Create your views here.
def index(request):
    tittle = 'Welcome to django coruse'
    return render(request,'index.html',{
        'titulo': tittle,
    })

def about(request):
    username='lucas'
    return render(request,'about.html',{
        'username': username,
    })

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" %username)

def projects(request):
    proyectos=list(Project.objects.values())
    projects=Project.objects.all()
    ##return JsonResponse(proyectos, safe=False)
    return render(request,'projects.html',{
        'proyectos': projects,
    })

def tasks(request):
    #tarea=Task.objects.get(id=id)
    #tarea=get_object_or_404(Task,id=id)
    #return HttpResponse("task: %s" %tarea.title)
    tareas=Task.objects.all()
    return render(request,'tasks.html',{
        'tareas': tareas,
    })
