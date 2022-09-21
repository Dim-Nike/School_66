from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.urls import path


urlpatterns = [
    path('/', views.title_news, name='title_news'),
    path('<int:pk>', views.DetailNews.as_view(), name='detail-news')


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)