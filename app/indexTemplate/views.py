from django.shortcuts import render, redirect
from django.contrib import messages
from users.models import User
from indexTemplate.form import LoginForm


def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'GET':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.get(email=email):
                messages.success(request, f'Logueado {email}')
                return redirect('index')
    return render(request, 'formLoginUser.html', {'form': form})
