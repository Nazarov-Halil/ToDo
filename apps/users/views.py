from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.views.generic import ListView


def logout_logics(request):
    logout(request)
    return redirect('list_todo')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password != repassword:
            return render(request, 'ToDo_User/sign_up.html', {'error': "Пароли не совподают !"})

        if User.objects.filter(username=username).exists():
            return render(request, 'ToDo_User/sign_up.html', {'error': "Такой пользватель уже есть !"})
        user = User.objects.create_user(
            username=username,
            password=password,
        )
        login(request, user)
        return redirect('/')
    return render(request, 'ToDo_User/sign_up.html')



def login_logics(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        error = "Incorrect password or login"
        return render(request, 'ToDo_User/sign_in.html', locals())
    return render(request, 'ToDo_User/sign_in.html')

