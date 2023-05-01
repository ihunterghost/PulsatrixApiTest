from django.shortcuts import render
from rest_framework import viewsets
from .serializers import logSerializer
from .models import log

class logViewSets(viewsets.ModelViewSet):
    queryset = log.objects.all()
    serializer_class = logSerializer