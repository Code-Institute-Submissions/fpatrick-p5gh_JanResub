from django import forms
from django.core.exceptions import ValidationError

from .models import Testimonial


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'message', 'rating']

    def clean_rating(self):
        data = self.cleaned_data['rating']

        if data:
            if data < 1:
                raise ValidationError(('Please enter a rating between 1 and 10'))

            if data > 10:
                raise ValidationError(('Please enter a rating between 1 and 10'))

        return data

