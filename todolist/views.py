from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import TodoItem

def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todolist/todo.html',
                  {'all_items':all_todo_items})


def addtodo(request):
    new_item = TodoItem(contents = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')


def deletecompleted(request):
    TodoItem.objects.filter(complete__exact=True).delete()
    return HttpResponseRedirect('/todo/')
def deleteall(request):
    TodoItem.objects.all().delete()
    return HttpResponseRedirect('/todo/')

def complete(request,item_id):
    complete_item = TodoItem.objects.get(id=item_id)
    complete_item.complete = True
    complete_item.save()
    return HttpResponseRedirect('/todo/')
