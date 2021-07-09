from django.shortcuts import render
from rest_framework import generics, serializers
from .serializers import UserDetailsSerializer
from .models import UserDetails
# Create your views here.

class StateMatch(generics.ListCreateAPIView):

    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer


class UpdateState(generics.RetrieveUpdateDestroyAPIView):

    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer
