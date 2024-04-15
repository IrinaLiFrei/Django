import datetime

from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import logging

from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import models
from .models import Order, Product
from .forms import EditProductForm, RegistrationForm, LoginForm

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse('Welcome to my SHOP!')


def about(request):
    logger.debug('About page accessed')
    return HttpResponse('This is the ABOUT page.')


def contact(request):
    logger.debug('Contact page accessed')
    return HttpResponse('This is the CONTACT page.')


def order_info(request):
    logger.debug('Orders info page accessed')
    return HttpResponse('This is the ORDERS info page. '
                        'If you want to see the orders by client ID, go to /order/client_id')


# Доработаем задачу 8 из прошлого семинара про клиентов, товары и заказы.
# Создайте шаблон для вывода всех заказов клиента и списком товаров внутри каждого заказа.
# Подготовьте необходимый маршрут и представление.
# Создайте шаблон, кот. выводит список заказанных клиентом товаров из всех его заказов с сортировкой по времени:
# ○ за последние 7 дней (неделю)
# ○ за последние 30 дней (месяц)
# ○ за последние 365 дней (год)
# *Товары в списке не должны повторятся.


def all_orders(request, client_id):
    logger.info(f'Client {client_id} orders page accessed')
    client = get_object_or_404(models.Client, pk=client_id)
    orders = Order.objects.filter(client=client)
    return render(request, 'shop_app/all_orders.html', {'client': client, 'orders': orders})


def orders_for_period(request, client_id, period):
    logger.info(f'Client {client_id} orders for time period page accessed')
    client = get_object_or_404(models.Client, pk=client_id)
    orders = Order.objects.filter(client=client)
    now = datetime.date.today()
    if period == 'week':
        requested_period = now - datetime.timedelta(days=7)
    elif period == 'month':
        requested_period = now - datetime.timedelta(days=30)
    elif period == 'year':
        requested_period = now - datetime.timedelta(days=365)
    ordered_products = Product.objects.filter(order__in=orders,
                                              order__order_date__range=[requested_period, now]).distinct()
    context = {
        'client_id': client_id,
        'period': requested_period,
        'ordered_products': ordered_products
    }
    return render(request, 'shop_app/orders_for_period.html', context)


def orders_for_days(request, client_id, days):
    logger.info(f'Client {client_id} orders for time period page accessed')
    client = get_object_or_404(models.Client, pk=client_id)
    orders = Order.objects.filter(client=client)
    now = datetime.date.today()
    requested_period = now - datetime.timedelta(days=days)
    ordered_products = Product.objects.filter(order__in=orders,
                                              order__order_date__range=[requested_period, now]).distinct()
    context = {
        'client_id': client_id,
        'period': requested_period,
        'ordered_products': ordered_products
    }
    return render(request, 'shop_app/orders_for_period.html', context)


# Создайте форму для редактирования товаров в базе данных.
# Измените модель продукта, добавьте поле для хранения фотографии продукта.
# Создайте форму, которая позволит сохранять фото.


def edit_form(request, product_id):
    product = get_object_or_404(models.Product, pk=product_id)
    if request.method == 'POST':
        form = EditProductForm(request.POST, request.FILES)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.stock = form.cleaned_data['stock']
            product.entry_date = form.cleaned_data['entry_date']
            product.product_image = form.cleaned_data['photo']
            product.save()
            message = f'Товар {product.name} изменен.'
            if 'photo' in request.FILES:
                product.product_image = request.FILES['photo']
                product.save()
    else:
        initial_data = {
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'stock': product.stock,
            'entry_date': product.entry_date,
            'image': product.product_image,
        }
        form = EditProductForm(initial=initial_data)
        message = f'Внесите изменения в товар {product.id} - {product.name}.'
    return render(request, 'shop_app/edit_form.html', {'form': form, 'message': message})


# Форма авторизации и кнопка выхода
class CustomLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'shop_app/login.html'
    extra_context = {'title': 'Авторизация на сайте'}

    def get_success_url(self):
        return reverse_lazy('index')

# Форма регистрации


class CustomRegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'shop_app/reg_form.html'
    extra_context = {'title': 'Регистрация на сайте'}

    def get_success_url(self):
        return reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)

###############################################################################
