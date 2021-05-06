from django.shortcuts import render, redirect
from django.contrib import messages
from users.models import User
from users.form import UserForm

# Create your views here.
def listUser(request):
    #Listar users
    #para enviarlo a la vista se una context el cual es un dictinary
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'listUser.html', context)

def createUser(request):
    #crear usuario
    if request.method == 'GET':
        form = UserForm()
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username}')
            return redirect('index')
    return render(request, 'formCreateUser.html', {'form': form})

def updateUser(request, id):
    user = User.objects.get(id = id)
    if request.method == 'GET':
        form = UserForm(instance = user)
    else:
        form = UserForm(request.POST, instance = user)
        if form.is_valid():
            form.save()
            return redirect('list_user')
    return render(request, 'formCreateUser.html', {'form': form})

def deleteUser(request, id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect('list_user')

def profile(request):
    return render(request, 'profile.html')