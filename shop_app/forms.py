# Создайте форму для редактирования товаров в базе данных.
# Измените модель продукта, добавьте поле для хранения фотографии продукта.
# Создайте форму, которая позволит сохранять фото.

from django import forms


class EditProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    stock = forms.IntegerField()
    entry_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    photo = forms.ImageField(required=False)


class ImageForm(forms.Form):
    image = forms.ImageField(required=False)


