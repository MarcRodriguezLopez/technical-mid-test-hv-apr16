from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Inspection
from .serializers import InspectionSerializer

@api_view(['GET'])
def inspecions_list(request, company='SolarGrade'):
    if request.method == 'GET':
        inspections = Inspection.objects.all()
        serializer = InspectionSerializer(inspections, many=True)
        return Response(serializer.data)