from django.shortcuts import render
from rest_framework import viewsets, permissions,generics
from .models import Event
from .serializers import EventSerializer

# Create your views here.




class EventListView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer