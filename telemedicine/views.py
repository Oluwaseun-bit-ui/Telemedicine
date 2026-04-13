from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Telemedicine API is running"
    })
