from django.urls import path
from .views import doctor_list_create, doctor_detail

urlpatterns = [
    path('', doctor_list_create),
    path('<int:pk>/', doctor_detail),
]
