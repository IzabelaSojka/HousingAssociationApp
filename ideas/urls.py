from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import path

from django.contrib.auth import views as auth_views
from . import views
from .notification import showFirebaseJS
from .view.local_views import local, local_delete
from .view.user_views import RegisterPage
from .view.resident_views import resident, resident_detail
from .view.administrator_views import administrator, adminEmail
from .view.document_views import fileView
from .view.user_views import editUser
from .view.billing_views import billing_history, billing_update, billing, billing_detail, resident_billing, resident_billing_history


urlpatterns = [
    path('home/', views.home, name='home'),

    #local
    path('local/', local, name='local'),
    path('local_delete/<int:pk>', local_delete, name='local_delete'),

    #billing
    path('billing/', billing, name='billing'),
    path('billing_update/<int:pk>', billing_update, name='billing_update'),
    path('billing_history', billing_history, name='billing_history'),
    path('billing_detail/<int:pk>', billing_detail, name='billing_detail'),

    #resident
    path('resident/', resident, name='resident'),
    path('resident_billing/', resident_billing, name='resident_billing'),
    path('resident_detail/<int:pk>', resident_detail, name='resident_detail'),

    #user
    path('register/', RegisterPage.as_view(), name='register'),
    path('', auth_views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('editUser/', editUser, name='edit_user'),
    path('gologin/', adminEmail, name='go_login'),
    path('adminDetail/', administrator, name='admin_detail'),

    #document
    path('documents/', fileView, name='documents'),

    #other
    path('firebase-messaging-sw.js', showFirebaseJS, name="show_firebase_js"),





]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)