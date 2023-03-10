from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm


def all_products(request):
    """View to show all products, including sorting and search queries."""
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

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
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(
        product=product).order_by('-created_on')

    review_form = ReviewForm(data=request.POST)

    context = {
        'product': product,
        'review_form': review_form,
        'reviews': reviews,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def edit_review(request, product_id):
    """ Edit a review in the store """

    # product = get_object_or_404(Product, pk=product_id)
    review = get_object_or_404(Review, id=product_id)
    product = review.product
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update review. Please ensure the form is valid.')
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing {product.name} review')

    template = 'products/edit_review.html'
    context = {
        'form': form,
        'product': product,
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def delete_review(request, product_id):
    """ Delete a review from the store """

    review = get_object_or_404(Review, id=product_id)
    product = review.product
    review.delete()
    new_total_rating = product.total_rating - review.rating
    Product.objects.filter(id=product.id).update(total_rating=new_total_rating)
    messages.success(request, 'Review deleted!')
    return redirect(reverse('product_detail', args=[product.id]))


def add_review(request, product_id):
    """ Add a product review """

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            exist_review = Review.objects.filter(product=product, user=request.user)
            if not exist_review:
                Review.objects.create(
                    product=product,
                    user=request.user,
                    title=request.POST['title'],
                    review=request.POST['review'],
                    rating=request.POST['rating'],
                )
                reviews = Review.objects.filter(product=product)

                rating_average = calc_rating(reviews, product)
                Product.objects.filter(id=product.id).update(total_rating=rating_average)

                messages.success(
                    request, 'Your review has been successfully added!')
            else:
                messages.error(request, 'You have already reviewed this product!')
            return redirect(reverse('product_detail', args=[product.id]))

        messages.error(request, 'Your review could not be validated')
    messages.error(request, 'Error submitting review')
    return redirect(reverse('product_detail', args=[product.id]))


def calc_rating(reviews, product):
    """ Calculate total rating """

    all_reviews = Review.objects.filter(product=product)

    number_reviews = len(all_reviews)
    total_ratings = 0
    for review in reviews:
        total_ratings += review.rating

    if number_reviews > 0:
        average_rating = (total_ratings / number_reviews)
        return average_rating
