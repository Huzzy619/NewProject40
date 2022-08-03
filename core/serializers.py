# from itsdangerous import Serializer
from rest_framework.serializers import ModelSerializer
from .models import *


class SchoolSerializer (ModelSerializer):

    class Meta:
        model = School
        fields = ['id', 'reg_number', 'name', 'email',
                  'category', 'LGA', 'address', 'user']


class ParentSerializer (ModelSerializer):

    class Meta:
        model = Parent
        fields = ['id', 'name', 'user_id']
