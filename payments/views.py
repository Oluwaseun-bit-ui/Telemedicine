from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Payment
from .serializers import PaymentSerializer


# LIST + CREATE PAYMENT
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def payment_list_create(request):
    if request.method == 'GET':
        payments = Payment.objects.filter(user=request.user)
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data.copy()
        data['user'] = request.user.id

        serializer = PaymentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


# 🔹 GET SINGLE PAYMENT
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def payment_detail(request, pk):
    try:
        payment = Payment.objects.get(pk=pk, user=request.user)
    except Payment.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    serializer = PaymentSerializer(payment)
    return Response(serializer.data)


# NEW: VERIFY PAYMENT
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def verify_payment(request):
    reference = request.data.get("transaction_reference")

    # ADDED: check if reference is provided
    if not reference:
        return Response({"error": "Transaction reference is required"}, status=400)

    try:
        payment = Payment.objects.get(
            transaction_reference=reference,
            user=request.user   # ADDED: security check
        )
    except Payment.DoesNotExist:
        return Response({"error": "Payment not found"}, status=404)

    # TEMP VERIFICATION LOGIC (before Paystack)
    payment.status = "successful"
    payment.save()

    # UPDATE APPOINTMENT STATUS
    appointment = payment.appointment
    appointment.status = "confirmed"
    appointment.save()

    return Response({"message": "Payment verified successfully"})