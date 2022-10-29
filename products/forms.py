from .models import Product
from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'category',
            'avenger',
            'name',
            'description',
            'price',
            )

        labels = {
            'category': 'Category',
            'avenger': 'Avenger',
            'name': 'Name',
            'description': 'Description',
            'price': 'Price',
        }

        widgets = {
            'category': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select Category',
                    'required': 'true'
                    }
                ),
            'avenger': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select Avenger',
                    'required': 'true'
                    }
                ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter item name',
                    'required': 'true'
                    }
                ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Tell us about this item, where did you find it, why is the item awesome?',  # noqa
                    'required': 'true'}
                ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Price',
                    'required': 'true'}
                ),
        }
