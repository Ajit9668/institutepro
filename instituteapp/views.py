from django.shortcuts import render, redirect
from .models import course,feedback,s_table
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
import datetime
date1=datetime.datetime.now()

@login_required(login_url='/instituteapp/login/')
def homeview(request):
    return render(request,'instituteapp/homepage.html')

@login_required(login_url='/instituteapp/login/')
def contactview(request):
    if request.method=='GET':
        return render(request, 'instituteapp/contactpage.html')
    else:
        s_table(first_name=request.POST['fname'],
        last_name=request.POST['lname'],
        email=request.POST['email'],
        mobile=request.POST['mobile'],
        course=request.POST['course'],
        location=request.POST['location']).save()
        return render(request, 'instituteapp/contactpage.html')

@login_required(login_url='/instituteapp/login/')
def serviceview(request):
    data=course.objects.all()
    return render(request, 'instituteapp/servicepage.html',{'data':data})

@login_required(login_url='/instituteapp/login/')
def feedbackview(request):
    if request.method=='GET':
        data=feedback.objects.all()
        return render(request, 'instituteapp/feedbackpage.html',{'data':data})
    else:
        feedback(comment=request.POST['comment'],date=date1).save()
        data=reversed(feedback.objects.all())
        return render(request, 'instituteapp/feedbackpage.html',{'data':data})

@login_required(login_url='/instituteapp/login/')
def galleryview(request):
    return render(request, 'instituteapp/gallerypage.html')

def loginview(request):
    if request.method=='GET':
        return render(request, 'instituteapp/loginpage.html')
    else:
        user=request.POST['username']
        pwd=request.POST['password']
        user=authenticate(request, username=user, password=pwd)
        if user is not None:
            login(request, user)
            return redirect(homeview)
        else:
            return HttpResponse('Invalid user & password')

def logoutview(request):
    logout(request)
    return redirect(loginview)

def registerview(request):
    if request.method=='GET':
        form=RegistrationForm()
        return render(request, 'instituteapp/registerpage.html',{'form':form})
    else:
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(user.password)
            form.save()
            return redirect(loginview)
        else:
            return HttpResponse('Invalid details')





