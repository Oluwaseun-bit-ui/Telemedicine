from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    sender_email = serializers.CharField(source= 'sender.email', read_only=True)
    class Meta:
        model = Message
        fields = '__all__'
