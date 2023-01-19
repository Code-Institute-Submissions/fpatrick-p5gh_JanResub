from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse

from products.models import Product
from wishlist.models import Wishlist


@login_required
def add_to_wishlist(request, product_id):
    """
    This view adds a product to the user's wishlist
    and redirects the user to the product detail page.
    If the product is already in the user's wishlist,
    it displays an error message
    """
    product = get_object_or_404(Product, pk=product_id)
    exist_wishlist_item = Wishlist.objects.filter(product=product, user=request.user)
    if not exist_wishlist_item:
        Wishlist.objects.create(
            product=product,
            user=request.user,
        )

        messages.success(
            request, 'The product has been successfully added to your wishlist!')
    else:
        messages.error(request, 'You have already added this product in your wishlist!')

    return redirect(reverse('product_detail', args=[product_id]))


@login_required
def wishlist(request):
    """
    This view displays the user's wishlist
    """
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})


@login_required
def remove_from_wishlist(request, product_id):
    """
        This view removes a product from the user's wishlist
        and redirects the user to the wishlist page.
    """
    Wishlist.objects.filter(user=request.user, product_id=product_id).delete()
    messages.success(request, 'Item removed from your wishlist!')
    return redirect(reverse('wishlist'))
