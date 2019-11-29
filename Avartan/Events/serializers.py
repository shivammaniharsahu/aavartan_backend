from rest_framework import serializers
from .models import Event
from rest_framework import status
from rest_framework.response import Response

class EventSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Event
        fields = ('title' ,'venue', 'poster_img', 'thumbnail_img', 'n_rounds', 'description', 'rules', 'instructions')