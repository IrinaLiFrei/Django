import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import logging
from . import models
from .models import Order, Product

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
    elif period =='month':
        requested_period = now - datetime.timedelta(days=30)
    elif period == 'year':
        requested_period = now - datetime.timedelta(days=365)
    ordered_products = Product.objects.filter(order__in=orders, order__order_date__range=[requested_period, now]).distinct()
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
    ordered_products = Product.objects.filter(order__in=orders, order__order_date__range=[requested_period, now]).distinct()
    context = {
        'client_id': client_id,
        'period': requested_period,
        'ordered_products': ordered_products
    }
    return render(request, 'shop_app/orders_for_period.html', context)
