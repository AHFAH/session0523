
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from coplate.views import CustomPasswordChangeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('allauth.urls')),
    path('', include('coplate.urls')),
    path("email-confirmation-done/", 
        TemplateView.as_view(template_name="coplate/email_confirmation_done.html"),
        name= "account_email_confirmation_done"),
    path('password/change/',CustomPasswordChangeView.as_view(), name="account_charge_password")
]
