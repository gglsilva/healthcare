# serializers.py
from ninja import Schema, ModelSchema
from .models import Exam

class ExamSerializer(Schema):
    name: str

class ExamResponseSerializer(ModelSchema):
    
    class Meta:
        model = Exam
        fields = ['name', 'created_at', 'updated_at']