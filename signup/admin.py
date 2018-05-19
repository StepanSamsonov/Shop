from django.contrib import admin
from .models import *


class UserAddedDataAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserData._meta.fields]
    # del list_display[list_display.index('liked_data')]
    # del list_display[list_display.index('order_data')]
    search_fields = ['owner_name']

    class Meta:
        model = UserData


admin.site.register(UserData, UserAddedDataAdmin)
