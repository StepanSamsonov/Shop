from django.db import models


class UserAddedData(models.Model):
    owner_name = models.CharField(max_length=100, blank=True, null=True, default=None)
    liked_data = models.TextField(blank=True, null=True, default=None)
    order_data = models.TextField(blank=True, null=True, default=None)
    created = models.TimeField(auto_now_add=True, auto_now=False)
    updated = models.TimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Дополнительно для ' + self.owner_name

    class Meta:
        verbose_name = 'Дополнительно'
        verbose_name_plural = 'Дополнительно'
