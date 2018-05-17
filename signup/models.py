from django.db import models


class LikedProducts(models.Model):
    owner_name = models.CharField(max_length=100, blank=True, null=True, default=None)
    liked_data = models.TextField(blank=True, null=True, default=None)
    created = models.TimeField(auto_now_add=True, auto_now=False)
    updated = models.TimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Избранное для ' + self.owner_name

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
