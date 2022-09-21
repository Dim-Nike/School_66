from django.contrib import admin
from .models import *


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'catClassUser']
    list_filter = ['date', 'catClassUser']


admin.site.register(UserClass)
admin.site.register(CustomUser)
