from django.db import models

# Create your models here.

class Inspection(models.Model):
    title = models.CharField(max_length=256)
    inspectorName = models.CharField(max_length=256)
    itemsOk = models.IntegerField()
    issuesWarningCount = models.IntegerField(blank=True, default=0)
    issuesCriticalCount = models.IntegerField(blank=True, default=0)
    company = models.CharField(max_length=256)