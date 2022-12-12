from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import path

from django.contrib.auth import views as auth_views
from . import views
from .notification import showFirebaseJS
from .views import *

urlpatterns = [
    path('home/', views.home, name='home'),
    path('local/', views.local, name='local'),
    path('local_delete/<int:pk>', views.local_delete, name='local_delete'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('billing/', views.billing, name='billing'),
    path('resident/', views.resident, name='resident'),
    path('billing_update/<int:pk>', views.billing_update, name='billing_update'),
    path('', auth_views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('editUser/',views.editUser, name='edit_user'),
    path('adminDetail/',views.administrator, name='admin_detail'),
    path('resident_billing/',views.resident_billing, name='resident_billing'),
    path('billing_history', billing_history, name='billing_history'),
    path('firebase-messaging-sw.js', showFirebaseJS, name="show_firebase_js"),
    path('documents/', views.fileView, name='documents'),
    path('billing_detail/<int:pk>', views.billing_detail, name='billing_detail'),
    path('resident_detail/<int:pk>', views.resident_detail, name='resident_detail'),
    path('gologin/', views.adminEmail, name='go_login')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)