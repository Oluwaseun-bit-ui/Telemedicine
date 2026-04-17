from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Doctor
from .serializers import DoctorSerializer

@api_view(['GET', 'POST'])
def doctor_list_create(request):
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
@api_view(['GET'])
def doctor_detail(request, pk):
    try:
        doctor = Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return Response({"error": "Doctor not found"}, status=404)

    serializer = DoctorSerializer(doctor)
    return Response(serializer.data)