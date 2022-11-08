from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='product_name')
    code = models.CharField(max_length=255, verbose_name='product_code')
    prise = models.DecimalField(max_digits=20, decimal_places=2)
    unit = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return f'{self.name}, {self.code}, {self.prise}, {self.note}'


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    time = models.DateField(auto_now_add=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return f'{self.user}, {self.amount}, {self.time},'


class Order(models.Model):
    STATUS_CART = '1_cart'
    STATUS_WAITING_FOR_PAYMENT = '2_waiting_for_payment'
    STATUS_PAID = '3_paid'
    STATUS_CHOICES = [
        (STATUS_CART, 'cart'),
        (STATUS_WAITING_FOR_PAYMENT, 'waiting_for_payment'),
        (STATUS_PAID, 'paid')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default=STATUS_CART)
    amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    creation_time = models.DateField(auto_now_add=True)
    payment = models.ForeignKey(Payments, on_delete=models.PROTECT, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return f'{self.user}, {self.status}, {self.amount}, {self.creation_time}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    prise = models.DecimalField(max_digits=20, decimal_places=2)
    discount = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return f'{self.product}, {self.prise}'





