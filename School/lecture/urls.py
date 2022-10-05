from django.conf.urls.static import static
from django.conf import settings
from .views import *
from django.urls import path, include



urlpatterns = [
    path('', landing, name='landing'),
    path('cat/<int:sub_id>/', detailLectureTopic, name='details_lecture'),
    path('lesson/<int:sub_id>', detailLesson, name='detail_lesson'),
    path('test/<int:sub_id>', show_test, name='test'),
    path('result', show_result_test, name='result_test')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)