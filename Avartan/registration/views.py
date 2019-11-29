from rest_framework import viewsets, permissions,generics
from registration.models import User
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Events.models import Event

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OTPView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user= request.user
        otp = request.GET['otp']
        if user.otp == int(otp):
            user.is_verified = True
            user.save()
            message = "User verified Successfully"
        else:
            message = "OTP verification failed"

        content = {'message':message}
        return Response(content)


class EventRegView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user= request.user
        event_id = int(request.GET['event_id'])
        if user.is_verified == True:
            event = Event.objects.get(id=event_id)
            if event in user.events.all():
                message = "You are already registered"
            else:
                user.events.add(event)
                user.save()
                message = "You are sucessfully Registered"
        else:
            message = "Please Verify first"

        content = {'message':message}
        return Response(content)


class EventListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    def get(self, request):
        user= request.user
        if user.is_verified == True:
            queryset = user.events.all()
            d = {'events':[]}
            for i in queryset:
                d['events'].append(i.id)
        return Response(d)
