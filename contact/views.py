from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here.

def message(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        phone = request.POST.get('Phone')
        email = request.POST.get('Email')
        message = request.POST.get('Message')
        submit = Contact(
            name = Name, phone = Phone, email = Email, message = Message
        )

        submit.save()
        return render(request, 'contact/contact.html')
    else:
        return render(request, 'contact/contact.html')    
