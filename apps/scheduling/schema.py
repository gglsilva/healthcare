from ninja import Schema, ModelSchema
from .models import Scheduling


class NotFoundResponse(Schema):
    detail: str

class SchedulingSchema(ModelSchema):
    class Meta:
        model = Scheduling
        fields = ['patient', 'exam', 'preference', 'status', 'scheduled_to', 'created_at', 'updated_at']