from rest_framework import serializers
from .models import Inspection

class InspectionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=256)
    inspectorName = serializers.CharField(max_length=256)
    itemsOk = serializers.IntegerField()
    issuesWarningCount = serializers.IntegerField(default=0)
    issuesCriticalCount = serializers.IntegerField(default=0)
    company = serializers.CharField(max_length=256)

    def create(self, validated_data):
        return Inspection.objects.create(**validated_data)