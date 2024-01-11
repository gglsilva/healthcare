from ninja import Schema, ModelSchema
from .models import Scheduling
from datetime import date


class NotFoundResponse(Schema):
    detail: str

class SchedulingSerializer(Schema):
    id: int
    patient: int
    exam: int
    preference: str
    status: str
    scheduled_to: date
    created_at: str
    updated_at: str
class SchedulingSchema(ModelSchema):
    class Meta:
        model = Scheduling
        fields = ['patient', 'exam', 'preference', 'status', 'scheduled_to', 'created_at', 'updated_at']