from django.conf.urls.static import static
from django.conf import settings
from .views import *
from django.urls import path


urlpatterns = [
    path('/', loginUser, name='login'),
    path('/reg', RegisterUser.as_view(), name='register')


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)