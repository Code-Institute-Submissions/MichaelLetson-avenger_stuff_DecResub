from django.shortcuts import render
from django.contrib import messages
from .models import Contact

# Create your views here.

def about(request):
    """ View to return about page """

    return render(request, 'about/about.html')

def contact_us(request):
    """ View to return contact us page and form """

    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        body = request.POST.get('body')
        contact.name = name
        contact.email = email
        contact.body = body
        contact.save()
        return render(request, 'about/contact_us.html')
    return render(request, 'about/contact_us.html')
