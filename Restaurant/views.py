from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Menu
from .serializers import MenuSerializer
from rest_framework import generics
from rest_framework import viewsets
from .models import Booking 
from .serializers import BookingSerializer 
# Create your views here.
# 
def index(request):
    return render(request, 'index.html', {})

class MenuView(generics.ListCreateAPIView):
 queryset = Menu.objects.all()
 serializer_class = MenuSerializer

class SingleMenuView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
 queryset = Menu.objects.all()
 serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer