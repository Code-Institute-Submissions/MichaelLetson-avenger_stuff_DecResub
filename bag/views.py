from django.shortcuts import render, redirect

# Create your views here.
def view_bag(request):
    """ View to return bag page to view items currently stored there """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)