from ninja import NinjaAPI
from .models import Patient
import json
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from .schema import PatientSchema

api = NinjaAPI()

@api.get('patient/')
def list(request):
    patients = Patient.objects.all()
    response = [{'patient_id': patient.patient_id, 'name': patient.name, 'age': patient.calculate_age(),'birth':patient.birth, 'gender': patient.gender}for patient in patients]
    return response

@api.get('patient/{id}')
def list_patient(request, id: int):
    patient = get_object_or_404(Patient, id=id)
    return model_to_dict(patient)
    
    
@api.post('patient/', response=PatientSchema)
def create(request, patient: PatientSchema):
    new_patient = patient.dict()
    patient = Patient(**new_patient)
    patient.save()
    return patient