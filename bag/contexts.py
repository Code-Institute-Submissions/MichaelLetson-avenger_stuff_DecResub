from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    if total < settings.DISCOUNTED_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        discounted_delivery_delta = settings.DISCOUNTED_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        discounted_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'discounted_delivery_delta': discounted_delivery_delta,
        'discounted_delivery_threshold': settings.DISCOUNTED_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context