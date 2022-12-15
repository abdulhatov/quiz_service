from django.urls import path

from .views import (
    AccountRegisterView,
    AccountLoginView,
)

app_name = 'account'

urlpatterns = [
    path('registration/', AccountRegisterView.as_view(), name='register'),
    path('', AccountLoginView.as_view(), name='login'),
]
