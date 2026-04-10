from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['POST'])
def register(request):
    data = request.data

    user = User.objects.create_user(
        email=data['email'],
        username=data['username'],
        password=data['password']
    )

    return Response({"message": "User created successfully"})