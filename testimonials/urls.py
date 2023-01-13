from django.urls import path
from . import views

urlpatterns = [
    path('testimonials/', views.testimonials, name='testimonials'),
    path('view_testimonial/', views.view_testimonial, name='view_testimonial'),
    path('add_testimonial/', views.add_testimonial, name='add_testimonial'),
]
