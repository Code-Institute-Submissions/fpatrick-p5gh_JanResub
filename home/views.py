from django.shortcuts import render

from testimonials.models import Testimonial


# Create your views here.


def index(request):
    """ A view to return the index page """
    latest_testimonials = Testimonial.objects.all().order_by('-created_at')[:3]
    more_testimonials = Testimonial.objects.all().order_by('-created_at')[3:6]
    return render(request, 'home/index.html', {'latest_testimonials': latest_testimonials,
                                               'more_testimonials': more_testimonials})
