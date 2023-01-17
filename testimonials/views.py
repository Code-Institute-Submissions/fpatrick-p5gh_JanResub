from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import TestimonialForm
from .models import Testimonial


# Create your views here.
def all_testimonials(request):
    testimonials_list = Testimonial.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(testimonials_list, 3)
    try:
        testimonials = paginator.page(page)
    except PageNotAnInteger:
        testimonials = paginator.page(1)
    except EmptyPage:
        testimonials = paginator.page(paginator.num_pages)

    return render(request, 'testimonials.html', {'testimonials': testimonials})


@login_required
def view_testimonial(request):
    try:
        testimonial = Testimonial.objects.get(user=request.user)
        return render(request, 'edit_testimonial.html', {'testimonial': testimonial})
    except Testimonial.DoesNotExist:
        return redirect('add_testimonial')


@login_required
def add_testimonial(request):
    try:
        Testimonial.objects.get(user=request.user)
        return redirect('edit_testimonial')
    except Testimonial.DoesNotExist:
        if request.method == 'POST':
            form = TestimonialForm(request.POST)
            if form.is_valid():
                testimonial = form.save(commit=False)
                testimonial.user_id = request.user.id
                testimonial.save()
                messages.success(request, 'Testimonial created successfully')
                return redirect('edit_testimonial')
            messages.error(request, 'Please enter a rating between 1 and 10!')
        else:
            form = TestimonialForm()
        return render(request, 'add_testimonial.html', {'form': form})


@login_required
def edit_testimonial(request):
    testimonial = Testimonial.objects.get(user=request.user)
    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, 'Testimonial updated successfully')
            return redirect('edit_testimonial')
        messages.error(request, 'Please enter a rating between 1 and 10!')
    else:
        form = TestimonialForm(instance=testimonial)
    return render(request, 'edit_testimonial.html', {'form': form, 'testimonial': testimonial})


@login_required
def delete_testimonial(request, testimonial_id):
    testimonial = Testimonial.objects.get(pk=testimonial_id)
    testimonial.delete()
    messages.success(request, 'Testimonial deleted successfully')
    return redirect('testimonials')
