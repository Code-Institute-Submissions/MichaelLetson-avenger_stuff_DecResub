from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

# Create your views here.

def about(request):
    """ View to return about page """

    return render(request, 'about/about.html')

def contact_us(request):
    """ View to return contact us page and contact us form """

    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        body = request.POST.get('body')
        contact.name = name
        contact.email = email
        contact.body = body
        contact.save()
        messages.success(request, f'Thanks, message received!')
        return render(request, 'about/contact_us.html')

    return render(request, 'about/contact_us.html')

def newsletter(request):
    """ View to return newsletter page and subscription form """
    if request.method == 'POST':
        form = NewsletterForm()
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        contact.name = name
        contact.email = email
        contact.address = address
        contact.save()
        messages.success(request, f'Thanks, message received!')
        return render(request, 'about/newsletter.html')

    return render(request, 'about/newsletter.html')