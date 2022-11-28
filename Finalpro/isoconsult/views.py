from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def ContactPage(request):
    if request.method == 'POST':
        address = request.POST['address']
        contact = request.POST['contact']
        position = request.POST['position']
        phone = request.POST['phone']
        email = request.POST['email']
        comemail = request.POST['comemail']
        message = request.POST['message']
        send_mail('Contact Form',
        message,'Company',
        [comemail,email],
        fail_silently=False)
    return render(request, 'iso/contact.html')

#ฟังก์ชัน HomePage
def HomePage(request):
    return render(request, 'iso/home.html')

def AboutPage(request):
    return render(request, 'iso/about.html')


def Register(request):
    if request.method == 'POST':
        data = request.POST.copy()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')

        newuser = User()
        newuser.username = email
        newuser.first_name = first_name
        newuser.last_name = last_name
        newuser.email = email
        newuser.set_password(password)
        newuser.save()
        return redirect('login')

    return render(request, 'iso/register.html')
