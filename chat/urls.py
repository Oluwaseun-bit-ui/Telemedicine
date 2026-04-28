from django.urls import path
from .views import chat_messages

urlpatterns = [
    path('<int:appointment_id>/', chat_messages),
]

