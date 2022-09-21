from django.conf.urls.static import static
from django.conf import settings
from .views import *
from django.urls import path, include



urlpatterns = [
    path('', landing, name='landing'),
    path('cat/<int:sub_id>/', detailLectureTopic, name='details_lecture'),
    path('lesson/<int:pk>', DetailLesson.as_view(), name='detail_lesson'),
    # path('login', logout_user, name='logout_user')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)