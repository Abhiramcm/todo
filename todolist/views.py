from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import TodoItem


def todoView(request):
    all_todo_items = TodoItem.objects.all()
    all_users =  User.objects.exclude(username='admin')
    tag = request.GET.get('tag_filter')
    if (tag == "All" or tag is None ):
        user_items = all_todo_items
    else:
        user_id = User.objects.get(username=tag).pk
        user_items = TodoItem.objects.filter(user=user_id)
    context = {'all_items': all_todo_items,
                   'users': all_users, 'useritems': user_items}
    return render(request, 'todolist/todo.html', context)

def user_login(request):
    context = {}
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request,username=username,password=password)
    if user:
        login(request, user)
        if username == 'admin':
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            else:
                return redirect('index')
        else:
            return redirect('index')
    else:
        context['error']="provide proper credentials!!"
        return render(request, 'todolist/login.html', context)

def user_logout(request):
        logout(request)
        return redirect('index')

@login_required(login_url='/user_login')
def addtodo(request):
    if (request.user.username == 'admin'):
        if request.method == "POST":
            content = request.POST.get('content')
            user_name = request.POST.get('tag')
            usr=User.objects.get(username=user_name)
            new_item = TodoItem(contents=content,user=usr)
            new_item.save()
            return redirect('index')
        else:
            return redirect('index')
    else:
        messages.info(request, 'Only admin can add todos!!')
        return redirect('index')

@login_required(login_url="/user_login/")
def deletecompleted(request):
    if (request.user.username == 'admin'):
        TodoItem.objects.filter(complete__exact=True).delete()
    else:
        messages.info(request, 'Only admin can delete todos!!')
    return redirect('index')

@login_required(login_url = "/user_login/")
def deleteall(request):
    if (request.user.username == 'admin'):
        TodoItem.objects.all().delete()
    else:
        messages.info(request, 'Only admin can delete todos!!')
    return redirect('index')
@login_required(login_url = "/user_login/")
def complete(request,item_id):
    if (request.user.username == 'admin'):
        complete_item = TodoItem.objects.get(id=item_id)
        complete_item.complete = True
        complete_item.save()
    else:
        messages.info(request, 'Only admin can toggle item status!!')
    return redirect('index')




