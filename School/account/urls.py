from django.conf.urls.static import static
from django.conf import settings
from .views import *
from django.urls import path

urlpatterns = [
  path('/', render_user, name='account'),
  path('send_mail', send_msg, name='send_mail'),
  path('send_notify', notify_mail, name='send_notify')


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)