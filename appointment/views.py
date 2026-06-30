from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Appointment
from .serializers import AppointmentSerializer

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def appointment_list_create(request):
    print("=" * 50)
    print("USER:", request.user)
    print("AUTH:", request.auth)
    print("HEADERS:", request.headers)
    print("=" * 50)

    if request.method == "GET":
        appointments = Appointment.objects.filter(user=request.user)
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

    data = request.data.copy()
    data["user"] = request.user.id

    serializer = AppointmentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def appointment_detail(request, pk):
    try:
        appointment = Appointment.objects.get(pk=pk, user=request.user)
    except Appointment.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    serializer = AppointmentSerializer(appointment)
    return Response(serializer.data)