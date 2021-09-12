from django.http import JsonResponse

# Create your views here.
def home(request):
    return JsonResponse({'message': 'Welcome to the E-commerce API'})