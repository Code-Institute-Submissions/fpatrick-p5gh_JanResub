from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UpdateTestimonialForm, TestimonialForm
from .models import Testimonial


# Create your views here.
def testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonials.html', {'testimonials': testimonials})


@login_required
def view_testimonial(request):
    try:
        testimonial = Testimonial.objects.get(user=request.user)
        return render(request, 'view_testimonial.html', {'testimonial': testimonial})
    except Testimonial.DoesNotExist:
        return redirect('add_testimonial')


@login_required
def add_testimonial(request):
    try:
        testimonial = Testimonial.objects.get(user=request.user)
        return render(request, 'view_testimonial.html', {'testimonial': testimonial})
    except Testimonial.DoesNotExist:
        if request.method == 'POST':
            form = TestimonialForm(request.POST)
            if form.is_valid():
                testimonial = form.save(commit=False)
                testimonial.user_id = request.user.id
                testimonial.save()
                messages.success(request, 'Testimonial created successfully')
                return redirect('view_testimonial')
        else:
            form = TestimonialForm()
        return render(request, 'add_testimonial.html', {'form': form})

