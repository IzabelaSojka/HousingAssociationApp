from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from django.contrib.auth import views as auth_views
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('local/', views.local, name='local'),
    path('local_delete/<int:pk>', views.local_delete, name='local-delete'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('billing/', views.billing, name='billing'),
    path('resident/', views.resident, name='resident'),
    path('billing_update/<int:pk>', views.billing_update, name='billing_update'),
    path('login/', auth_views.LoginView.as_view(), name='login'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)