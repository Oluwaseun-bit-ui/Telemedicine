from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['POST'])
def register(request):
    data = request.data

    email = data.get("email")

    if User.objects.filter(email=email).exists():
        return Response(
            {"error": "Email already exists"},
            status=400
        )

    user = User.objects.create_user(
        username=data.get("username"),
        email=email,
        password=data.get("password")
    )

    return Response({
        "message": "User created successfully"
    })