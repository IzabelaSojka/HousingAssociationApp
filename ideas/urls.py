from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('createLocal/', LocalCreate.as_view(), name='local'),
    path('createBilling/', BillingCreate.as_view(), name='billing'),
    path('listLocal/', LocalList.as_view(), name='locals'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)