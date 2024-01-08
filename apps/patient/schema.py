from ninja import Schema, ModelSchema
from .models import Patient
from uuid import UUID


class UUIDField(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        try:
            return str(uuid.UUID(v))
        except (TypeError, ValueError):
            raise ValueError("Invalid UUID format")

# antigo
# class PatientcShema(Schema):
#     name: str
#     cpf: str = None
#     birth: str = None
#     gender: str = None
#     # patient_id: UUIDField

class NotFoundResponse(Schema):
    detail: str

class PatientSchema(ModelSchema):
    class Meta:
        model = Patient
        fields = "__all__"