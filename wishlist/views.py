from django.shortcuts import render

from products.models import Product
from wishlist.models import Wishlist


# Create your views here.
def add_to_wishlist(request, product_id):
    user = request.user
    product = Product.objects.get(id=product_id)
    Wishlist.objects.create(user=user, product=product)
    return redirect('wishlist')


def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})


def remove_from_wishlist(request, product_id):
    Wishlist.objects.filter(user=request.user, product_id=product_id).delete()
    return redirect('wishlist')
