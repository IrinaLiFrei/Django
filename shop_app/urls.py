from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'shop_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('order/', views.order_info, name='orders_info'),
    path('order/<int:client_id>/', views.all_orders, name='all_orders'),
    path('order/<int:client_id>/<str:period>/', views.orders_for_period, name='orders_for_period'),
    path('order/<int:client_id>/days/<int:days>/', views.orders_for_days, name='orders_for_days'),
    path('product/edit/<int:product_id>', views.edit_form, name='edit_form'),
    path('login/', views.CustomRegistrationView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.CustomRegistrationView.as_view(), name='signup'),
]
