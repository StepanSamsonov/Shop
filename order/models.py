from django.db import models
from product.models import Product
from django.db.models.signals import post_save


class OrderStatus(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.TimeField(auto_now_add=True, auto_now=False)
    updated = models.TimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Статус: ' + self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class Order(models.Model):
    customer_name = models.CharField(max_length=100, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=50, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=200, blank=True, null=True, default=None)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(OrderStatus, blank=True, null=True, default=None)
    created = models.TimeField(auto_now_add=True, auto_now=False)
    updated = models.TimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Заказ id: ' + str(self.id)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    number = models.IntegerField(default=1)
    price_per_one = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created = models.TimeField(auto_now_add=True, auto_now=False)
    updated = models.TimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):
        self.price_per_one = self.product.price
        self.total_price = self.number*self.price_per_one
        super(ProductInOrder, self).save(*args, **kwargs)


def post_save_in_order(sender, instance, created, **kwargs):
    total_price = 0
    products = ProductInOrder.objects.filter(order=instance.order, is_active=True)
    for product in products:
        total_price += product.total_price

    instance.order.total_price = total_price
    instance.order.save(force_update=True)


post_save.connect(post_save_in_order, sender=ProductInOrder)
