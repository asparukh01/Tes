from rest_framework import serializers
from headhunter_app.models import *


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['id', 'title', 'description', 'users', 'begin_at', 'end_at']
        read_only_fields = ['id', 'users']

        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['id', 'title', 'description', 'types', 'status', 'project',]
        read_only_fields = ['id', 'types']
