from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'date']
    search_fields = ['title']


admin.site.register(News, NewsAdmin)

