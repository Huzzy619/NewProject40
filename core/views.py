from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *
# Create your views here.



class SchoolViewSet (ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class ParentViewSet (ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

    