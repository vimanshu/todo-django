from django.shortcuts import redirect, render, HttpResponse

# to make use of django's form api

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import authenticate, login as loginUser, logout as lg
from django.contrib.auth.decorators import login_required
from app.models import Todo
from app.forms import TodoForm

# creating my view...


def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'app/signup.html', {'form': form})
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')
                
            
        else:
            return render(request, 'app/signup.html', {'form': form})



def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'app/login.html', {'form': form})
    else:
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username =form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password= password)
            if user is not None:
                loginUser(request,user )
            return redirect('home')
        else:
            return render(request, 'app/login.html', {'form': form})

@login_required(login_url='login')
def welcome(request):
    if request.user.is_authenticated:
        user = request.user

    form = TodoForm()
    todos = Todo.objects.filter(user = user).order_by('priority')
    return render(request, 'app/welcome.html', {'form' : form, 'todos': todos})


def index(request):
    return render(request, 'app/index.html')

@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()

            print(todo)
            return redirect('home')
        else:
            return render(request, 'app/welcome.html', {'form':form})


def delete_todo(request, id):
    Todo.objects.get(pk = id).delete()
    return redirect('home')

def change_status(request,id, status):
    print(id,status)
    todo = Todo.objects.get(pk =id)
    todo.status = status
    todo.save()
    return redirect('home')

def logout(request):
    lg(request)
    return redirect('login')




