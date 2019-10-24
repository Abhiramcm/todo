from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import TodoItem


def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todolist/todo.html',
                  {'all_items':all_todo_items})

def user_login(request):
    context = {}
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request,username=username,password=password)
    if user and username=='admin':
        login(request, user)
        if request.GET.get('next', None):
            return HttpResponseRedirect(request.GET['next'])
            #return redirect('login')
        else:
            context['error']="provide proper credentials!!"
            return render(request,'login.html',context)
    else:
        return render(request, 'todolist/login.html', context)

@login_required(login_url='/user_login')
def addtodo(request):
    if request.method == "POST":
        n = request.POST.get('content')
        new_item = TodoItem(contents=n)
        new_item.save()
        return redirect('index')
    else:
        return redirect('index')

@login_required(login_url="/user_login/")
def deletecompleted(request):
    TodoItem.objects.filter(complete__exact=True).delete()
    return redirect('index')

@login_required(login_url = "/user_login/")
def deleteall(request):
    TodoItem.objects.all().delete()
    return redirect('index')
@login_required(login_url = "/user_login/")
def complete(request,item_id):
    complete_item = TodoItem.objects.get(id=item_id)
    complete_item.complete = True
    complete_item.save()
    return redirect('index')
