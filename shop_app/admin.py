from _decimal import Decimal
from django.contrib import admin
from .models import Client, Product, Order


@admin.action(description='Increase price by 10 percent')
def price_increase(modeladmin, request, queryset):
    for product in queryset.filter(stock__lt=5):
        product_price = float(product.price)
        increased_price = product_price + (product_price * 0.1)
        product.price = Decimal(str(increased_price))
        product.save()


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'reg_date')
    ordering = ('id',)
    search_fields = ('name', 'surname')
    search_help_text = 'Search by name or surname'
    readonly_fields = ['reg_date']
    fieldsets = [
        (None,
         {'classes': ['wide'],
          'fields': ['name'],
          }
         ),
        ('Personal data',
         {'fields': ['email', 'phone', 'address'],
          }
         ),
        ('Other data',
         {'fields': ['reg_date'],
          }
         ),
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock')
    # ordering = ('-published_at',)
    list_per_page = 15
    search_fields = ('name', 'description')
    search_help_text = 'Search by name or description'
    readonly_fields = ['entry_date']
    actions = [price_increase]
    fieldsets = [
        (None,
         {'classes': ['wide'],
          'fields': ['name'],
          }
         ),
        ('Details',
         {'fields': ['price'],
          }
         ),
        ('Stock',
         {'fields': ['stock'],
          }
         ),
        ('Description',
         {
             'classes': ['collapse'],
             'fields': ['description'],
         }
         ),
        ('Views and status',
         {'description': 'Views',
          'fields': ['entry_date', 'product_image'],
          }
         ),
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'total_price', 'order_date')
