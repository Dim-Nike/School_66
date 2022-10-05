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


class TestAdmin(admin.ModelAdmin):
    list_display = ['name_test', 'start_date', 'end_date', 'distance', 'is_active']
    list_filter = ['start_date', 'end_date', 'is_active']
    search_fields = ['name_test']
    filter_horizontal = ['answer']


class TestResultAdmin(admin.ModelAdmin):
    list_display = ['test', 'user', 'result_test', 'date_user', 'date']
    list_filter = ['test', 'date', 'user', 'class_user']
    search_fields = ['date']

class AskAdmin(admin.ModelAdmin):
    pass




class AnswerAdmin(admin.ModelAdmin):
    filter_horizontal = ['ask']


admin.site.register(Lecture, LectureAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Ask, AskAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(TestResult, TestResultAdmin)


