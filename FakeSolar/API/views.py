from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers

from .models import Inspection
from .serializers import InspectionSerializer
from .services import getInspectors

@api_view(['GET'])
def inspecions_list(request):
    if request.method == 'GET':
        company = request.query_params.get("company", 'SolarGrade')
        if company == 'SolarGrade':
            return Response(getInspectors())
        inspections = Inspection.objects.all()
        serializer = InspectionSerializer(inspections, many=True)
        return Response(serializer.data)