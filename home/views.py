from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail

from .forms import ClientForm


def home(request):
    return render(request, "index1.html")

def about(request):
    return render(request, "about.html")  


def form(request):
    form = ClientForm(request.POST)
    message = ''
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            send_mail(
                subject='SUCCESSFUL REGISTRATION',
                message='Welcome \n\nYou have successfully registered on the Ratna Nidhi portal! \n With your help, we will make this world a better one! \n',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[form.data['email']],
            )
            return redirect('index1')
        message = 'Oops! Something wasn\'t right.'
    return render(request, "Form.html", {'message': message})


def dash(request):
    return render(request, "dashboard.html")