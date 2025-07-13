from django import forms
from .models import Ad

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'price', 'location', 'image', 'category']
        widgets = {
            'title':       forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}),
            'price':       forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Цена'}),
            'location':    forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Город или район'}),
            'category':    forms.Select(attrs={'class': 'form-select'}),
            'image':       forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
