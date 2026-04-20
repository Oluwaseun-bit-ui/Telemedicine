from django.urls import path
from .views import appointment_list_create, appointment_detail

urlpatterns = [
    path('', appointment_list_create),
    path('<int:pk>/', appointment_detail),
]
