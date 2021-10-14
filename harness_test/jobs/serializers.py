from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from .models import Job, Skill

class SkillSerializer(ModelSerializer):
    """ Skill Model Serializer """
    class Meta:
        model = Skill
        fields = '__all__'
        
    def to_representation(self, instance):
        return {
            'name': instance.name
        }

class SkillReadSerializer(ModelSerializer):
    """ Skill Model Serializer """
    class Meta:
        model = Skill
        fields = '__all__'
        
    def to_representation(self, instance):
        return {
            'name': instance.name,
            'count': instance.num_job
        }

class JobOnlyReadSerializer(ModelSerializer):
    """ Job Model Serializer """
    skills = SkillSerializer(many=True, read_only=True)
    
    class Meta:
        model = Job
        fields = '__all__'
        
class JobSerializer(ModelSerializer):
    """ Job Model Serializer """
    skills = SkillSerializer(many=True)
    
    class Meta:
        model = Job
        fields = '__all__'
