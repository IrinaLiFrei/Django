from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    entry_date = models.DateField(auto_now_add=True)
    product_image = models.ImageField(blank=True, upload_to='products/')

    def __str__(self):
        return f'{self.name} / {self.price}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        li = []
        for product in self.products.all():
            li.append(product)

        return (f'{self.client.name}, список продуктов: {li}, сумма заказа: {self.total_price} руб., '
                f'дата заказа: {self.order_date}')
