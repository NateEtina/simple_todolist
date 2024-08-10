from django.shortcuts import render, redirect
from time import strftime

from .models import Task, Tasklist
from .forms import TasklistForm

# Create your views here.

def index(request):
    # current_date = strftime("%Y/%m/%d/")
    tasklists = Tasklist.objects.all() # Take every Tasklist occurences with their values
    tasklists_count = tasklists.count()
    list_tasklists = []
    for item in tasklists:
        list_tasklists.append((item, Task.objects.filter(parentlist__listTitle=str(item.listTitle)).count()))
    context = {
        'list_tasklists':list_tasklists,
        'tasklists_count':tasklists_count,
    }

    return render(request, 'base/home.html', context)

def addTaskList(request):
    form = TasklistForm()
    if request.method == 'POST':
        form = TasklistForm(request.POST)
        if form.is_valid():
            tasklist = form.save(commit=False)
            tasklist.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/tasklist_form.html', context)

def deleteTaskList(request, pk):
    tasklist = Tasklist.objects.get(id=pk)
    if request.method == 'POST' :
        tasklist.delete()
        return redirect('home')
    return render(request, 'base/delete_tasklist.html', {'obj':tasklist})

def updateList(request, pk):
    tasklist = Tasklist.objects.get(id=pk)
    form = TasklistForm(instance=tasklist)
    if request.method == 'POST' :
        form = TasklistForm(request.POST, instance=tasklist)
        if form.is_valid():
            form.save()

        return redirect('list', pk=tasklist.id)
    context = {'form':form}
    return render(request, 'base/tasklist_form.html', context)

def tasklist(request, pk):
    achievedTask = []
    unachievedTask = []
    tasklist = Tasklist.objects.get(id=pk)
    tasks = tasklist.task_set.all()

    for item in tasks:
        if item.completed == True :
            achievedTask.append(item)
        elif item.completed == False:
            unachievedTask.append(item)
    # task creation
    if request.method == 'POST':
        task = Task.objects.create(   
            parentlist = tasklist,
            taskline = request.POST.get('body')
        )
        return redirect('list', pk=tasklist.id)
    context = {
        'tasklist':tasklist,
        'tasks':tasks,
        'achievedTask' : achievedTask,
        'unachievedTask':unachievedTask,
    }
    return render(request, 'base/tasklist.html', context) 

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    tasklistId = task.parentlist.id
    #tasklistId = task.
    if request.method == 'POST' :
        task.delete()
        return redirect('list', pk=tasklistId)
    return render(request, 'base/delete_task.html', {'obj':task})

def completeTask(request, pk):
    task = Task.objects.get(id=pk)
    tasklistId = task.parentlist.id
    task.completed = True
    task.save()
    return redirect('list', pk=tasklistId)

'''def updateTask(request, pk):
    tasklist = Tasklist.objects.get(id=pk)
    form = TasklistForm(instance=tasklist)
    if request.method == 'POST' :
        form = TasklistForm(request.POST, instance=tasklist)
        if form.is_valid():
            form.save()

        return redirect('list', pk=tasklist.id)
    context = {'form':form}
    return render(request, 'base/tasklist_form.html', context)'''
