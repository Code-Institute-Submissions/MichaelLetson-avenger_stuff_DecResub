from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact, Newsletter, Review

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
        messages.success(request, ('Thanks, message received!'))
        return render(request, 'about/contact_us.html')

    return render(request, 'about/contact_us.html')

def newsletter(request):
    """ View to return newsletter page and subscription form """
    if request.method == 'POST':
        newsletterform = Newsletter()
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        newsletterform.name = name
        newsletterform.email = email
        newsletterform.address = address
        newsletterform.save()
        messages.success(
            request, ('You are now listed to receive the monthly newsletter!')
            )
        return render(request, 'about/newsletter.html')

    return render(request, 'about/newsletter.html')

def review(request):
    """ View to return page for users to leave a review """
    model = Review
    queryset = Review.objects.all()
    reviews = queryset.order_by("-created_on")

    if request.method == 'POST':
        reviewform = Review()
        name = request.POST.get('name')
        email = request.POST.get('email')
        body = request.POST.get('body')
        reviewform.name = name
        reviewform.email = email
        reviewform.body = body
        reviewform.save()
        messages.success(
            request, (
                'Your review has been posted and will appear below!'
                )
            )
        return render(request, 'about/review.html', {'reviews': reviews, })

    return render(
        request, 
        'about/review.html',
        {
            'reviews': reviews,
            }
        )

def delete_review(request, review_id=None):
    model = Review
    review_to_delete = Review.objects.get(id=review_id)
    review_to_delete.delete()
    messages.success(request, ('Review successfully deleted!'))

    return redirect('review')
