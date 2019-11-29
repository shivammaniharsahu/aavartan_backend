from rest_framework import serializers
from registration.models import User
from rest_framework import status
from rest_framework.response import Response
from .sms import send_sms
import random

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User(
            name=validated_data['name'],
            contact=validated_data['contact'],
            email=validated_data['email'],
            college=validated_data['college'],
            branch=validated_data['branch'],
            course=validated_data['course'],
            sem=validated_data['sem'],
            city=validated_data['city']
        )

        user.otp = random.randint(100000,999999)       
        user.set_password(validated_data['password'])
        user.username = str(user.contact)
        user.save()
        message = 'Your OTP is '+ str(user.otp)
        send_sms(user.contact, message)
        return user


    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ('password','name','email','contact',
            'college','branch','course','sem','city')