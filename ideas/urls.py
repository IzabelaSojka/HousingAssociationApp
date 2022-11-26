from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.home),
    path('local/', views.local, name='local'),
    path('register/', RegisterPage.as_view(), name='register'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)