from django.shortcuts import render,redirect
from blogwebsite.templates import * 
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from blogwebsite.models import *


User = get_user_model()

def index(request):

    queryset = Blog.objects.all()

    context = {'data' : queryset}

    return render(request,'index.html',context)

def createBlog(request):

    if request.method == 'POST':

        data = request.POST

        title = data.get('title')
        description = data.get('description')
        

        Blog.objects.create(
                user = request.user,
                title = title,
                description = description
                
        )

        return redirect ('index')

    return render(request,'createBlog.html')

def single_blog_view(request,pk):

    queryset = Blog.objects.get(id = pk)

    context = {'data': queryset}

    return render(request,'single_blog_view.html',context)

def update_blog(request,pk):
    queryset = Blog.objects.get(id = pk)

    if request.method == 'POST':

        title = request.POST.get('title')
        description = request.POST.get('description')

        queryset.title = title
        queryset.description = description

        queryset.save()
        return redirect('index')

    context = {'data': queryset}
    return render(request,'update_blog.html',context)

def delete_blog(request,pk):

    queryset = Blog.objects.get(id = pk)
    queryset.delete()
    return redirect('index')

def signin_page(request):

    if request.method == 'POST':

        data = request.POST

        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.error(request, "Username already exists.")
            return redirect('signin_page')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )

        user.set_password(password)
        user.save()
        

        return redirect('login_page')



    return render(request,'signin_page.html')

def login_page(request):

    if request.method == 'POST':

        data = request.POST

        username = data.get('username')
        password = data.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request,'Credentials are invalid')
            return redirect('login_page')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request,'Password is invalid')
            return redirect('login_page')
        else:
            login(request,user)
            return redirect('index')


    return render(request,'login_page.html')

def logout_page(request):
    logout(request)
    return redirect('login_page')