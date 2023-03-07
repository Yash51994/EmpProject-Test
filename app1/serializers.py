from app1.models import *
from rest_framework.serializers import ModelSerializer

class EmpSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'