from app1.models import *
from app1.serializers import EmpSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def show_data(request):
    emps = Employee.objects.all()
    ser = EmpSerializer(emps, many=True)
    return Response(ser.data)

