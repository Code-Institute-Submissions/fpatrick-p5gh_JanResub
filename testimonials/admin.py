from django.contrib import admin
from .models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('name', 'message')


admin.site.register(Testimonial, TestimonialAdmin)
