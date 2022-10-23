from django.shortcuts import render

# Create your views here.
def view_bag(request):
    """ View to return bag page to view items currently stored there """

    return render(request, 'bag/bag.html')