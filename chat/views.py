from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Message
from .serializers import MessageSerializer
from appointment.models import Appointment


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def chat_messages(request, appointment_id):

    try:
        appointment = Appointment.objects.get(pk=appointment_id)
    except Appointment.DoesNotExist:
        return Response({"error": "Appointment not found"}, status=404)

    # Only allow confirmed appointments
    if appointment.status != "confirmed":
        return Response({"error": "Chat only allowed for confirmed appointments"}, status=403)

    # Only patient or doctor can access
    if request.user != appointment.user and request.user != appointment.doctor.user:
        return Response({"error": "Not allowed"}, status=403)

    if request.method == 'GET':
        messages = Message.objects.filter(appointment=appointment)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = request.data.copy()
        data['sender'] = request.user.id
        data['appointment'] = appointment.id

        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)