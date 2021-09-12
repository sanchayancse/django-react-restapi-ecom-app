from django.urls import path, include
from rest_framework.authtoken import views
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('category/', include('api.category.urls')),


]
