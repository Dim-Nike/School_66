from django.contrib import admin
from .models import *


class LectureAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'cat', 'is_active']
    list_display_links = ['title', 'is_active']
    # search_fields = ['title', 'date']
    list_filter = ['date', 'is_active', 'cat']



class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name_subjects', 'userClass']
    list_filter = ['userClass']




admin.site.register(Lecture, LectureAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Test)
