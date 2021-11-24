from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.


def index(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'main/index.html', {'title': 'Main page', 'tasks': tasks})


def home(request):
    return render(request, 'main/about.html')


def verkopen(request):
    # if user send something (by method POST)
    if request.method == 'POST':
        # create an object on base of TaskForm class
        # and put into the data from user
        form = TaskForm(request.POST)
        # if all data from user are correct :
        if form.is_valid():
            # save data into bd
            form.save()
            # redirect user at home page
            redirect('home')


    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/verkopen.html', context)
