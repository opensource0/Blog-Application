from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from .models import BlogArticle

# Create your views here.

def index(request):
    blogs = BlogArticle.objects.all().order_by('title')
    context = {'blogs':blogs}
    return render(request,'testapp/home.html',context)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        fname = request.POST['fname']
        if User.objects.filter(email=email).exists():
            messages.error(request,'Email Is Taken ')
            return render(request,'testapp/register.html')
        elif User.objects.filter(username=username).exists():
            messages.error(request,'User Name Is Taken')
            return render(request,'testapp/register.html')
        else:
            user = User.objects.create_user(username=username,password=password,email=email,first_name=fname)
            user.save();
            messages.success(request,'Account Created Successful')
            return redirect('login')
    else:
        return render(request,'testapp/register.html')


def loginUser(request):
     blogs = BlogArticle.objects.all().order_by('title')
     if request.method == 'POST':
         username = request.POST['username']
         pwd = request.POST['password']
         user = authenticate(username=username,password=pwd)
         if user is not None:
             login(request,user)
             context =  { 'blogs' : blogs}
             return render(request,'testapp/home.html',context)
         else:
             messages.warning(request,'Data Is Not Correct')
             return render(request,'testapp/login.html')
     else:
         return render(request,'testapp/login.html')


def logoutUser(request):
     logout(request)
     messages.success(request,'Logout Successful')
     return redirect('/')


def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.info(request,'Update Successful')
            return redirect('/')
        else:
            messages.error(request,'Failed')
    else:
        form =PasswordChangeForm(request.user)
        context = {'form':form}
        return render(request,'testapp/changePassword.html',context)
        
def addBlog(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST['title']
            text = request.POST['text']
            author = request.POST['author']
            a = User.objects.get(username=author)
            if a is None:
                messages.info(request,'No User Found')
                return render(request)
                b = BlogArticle(title=title,author=a,text=text)
                b.save()
                messages.info(request,'Blog Add Successful')
                return render(request,'testapp/addBlog.html')
        else:
            return render(request,'testapp/addBlog.html')
    else:
        messages.info(request,'Please Login First')
        blogs = BlogArticle.objects.all().order_by('title')
        context = {'blogs':blogs}
        return render(request,'testapp/home.html',context)
