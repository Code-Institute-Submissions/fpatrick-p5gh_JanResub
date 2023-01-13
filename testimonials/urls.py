from django.urls import path
from . import views

urlpatterns = [
    path('testimonials/', views.testimonials, name='testimonials'),
    path('add_testimonial/', views.add_testimonial, name='add_testimonial'),
    path('edit_testimonial/', views.edit_testimonial, name='edit_testimonial'),
]
