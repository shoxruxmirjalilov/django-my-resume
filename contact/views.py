from django.shortcuts import render, redirect
from config.settings import EMAIL_HOST_USER
from . import forms 
from django.core.mail import send_mail
from django.utils import timezone
from contact.forms import MyCommentForm
from django.contrib import messages
from twilio.rest import Client

# Create your views here.

def contact(request):
    form = forms.Email()    
        
    context = {
        'form' : form,    
        }
    if request.method == 'POST':
        form = forms.Email(request.POST)
        subject = 'Xabaringiz muvafaqiyatli yuborildi!'
        message = request.POST.get('message')
        email = request.POST.get('email')
        send_mail(subject,
            message, EMAIL_HOST_USER, [email], fail_silently = False)  
        form = MyCommentForm(request.POST)     
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            messages.success(request, 'Xabaringiz muvafaqiyatli yuborildi!')
            return redirect('contact')
    else:
        form = MyCommentForm()    
    return render(request, 'contact.html', context)

 

