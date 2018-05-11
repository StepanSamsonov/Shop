from django.db import models


class PricePerSome(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default=None)
    created = models.TimeField(auto_now_add=True, auto_now=False)
    updated = models.TimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Цена за ' + self.name

    class Meta:
        verbose_name = 'Цена за ...'
        verbose_name_plural = 'Цены за ...'


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default=None)
    created = models.TimeField(auto_now_add=True, auto_now=False)
    updated = models.TimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_per_some = models.ForeignKey(PricePerSome, blank=True, null=True, default=None)
    characteristic = models.TextField(blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    category = models.ForeignKey(Category, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='product_images\\')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

