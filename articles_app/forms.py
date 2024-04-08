from django import forms
import datetime


class AuthorForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'placeholder': 'Enter your name'}))
    surname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'Enter your surname'}))
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'user@example.com'}))
    biography = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                                            'placeholder': 'Biography'}))
    date_of_birth = forms.DateField(initial=datetime.date.today(), widget=forms.DateInput(attrs={'class': 'form-control',
                                                                                             'type': 'date'}))
