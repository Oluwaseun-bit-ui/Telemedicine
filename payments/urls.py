from django.urls import path
from .views import payment_list_create, payment_detail, verify_payment

urlpatterns = [
    path('', payment_list_create),
    path('<int:pk>/', payment_detail),
    path('verify/', verify_payment), 
]
