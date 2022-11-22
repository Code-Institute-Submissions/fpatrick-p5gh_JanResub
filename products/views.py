from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from . models import Product, Category
# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    # To not get an error when loading page without a search term
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        # Check if sort is in the request of get
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            # Get sort into a new variable to preserve the original
            sort = sortkey
            if sortkey == 'name':
                # For the event of user sorting by name
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            # If category, the products.order_by will be category__name
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                # Check direction in order to decide whether to reverse the order
                if direction == 'desc':
                    # Minus in front means reverse
                    sortkey = f'-{sortkey}'
            # Finally, to really sort
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Use Q to match term of product name OR (instead of and) description
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show invididual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)