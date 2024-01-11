# from ninja import NinjaAPI
from ninja import Router
from .models import Patient
import json
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from .serializers import PatientSchema, NotFoundResponse
from django.http import JsonResponse
import uuid

# api = NinjaAPI()
router = Router()

@router.get('/', tags=["Patient"])
def list(request):
    patients = Patient.objects.all()
    response = [{'patient_id': patient.patient_id, 'name': patient.name, 'age': patient.calculate_age(),'birth':patient.birth, 'gender': patient.gender}for patient in patients]
    return response

@router.get('/{id}', tags=["Patient"])
def list_patient(request, id: int):
    patient = get_object_or_404(Patient, id=id)
    return model_to_dict(patient)
    
    
@router.post('/', response=PatientSchema, tags=["Patient"])
def create(request, patient: PatientSchema):
    new_patient = patient.dict()
    patient = Patient(**new_patient)
    patient.save()
    return patient

@router.put('/{id}', tags=["Patient"])
def update(request, id: int, data: PatientSchema):
    try:
        patient = Patient.objects.get(id=id)
        for attribute, value in data.dict().items():
            setattr(patient, attribute, value)
        patient.save()
        return 200, {"detail": "Paciente atualizado com sucesso"}
    except Patient.DoesNotExist as e:
        return 404, {"detail": "Paciente não encontrado"}
    # try:
    #     patient = Patient.objects.get(id=id)
    # except Patient.DoesNotExist:
    #     return 404, {"detail": "Paciente não encontrado"}
    
    # # Atualize os campos do paciente com os dados fornecidos
    # patient.name = data.name
    # patient.cpf = data.cpf
    # patient.birth = data.birth
    # patient.gender = data.gender

    # # Salve as alterações no paciente
    # patient.save()
    
    # return {"detail": "Paciente atualizado com sucesso"}
    
@router.delete("/{id}", tags=["Patient"], response={201: None, 404: NotFoundResponse})
def delete_patient(request, id: int):
    try:
        patient = Patient.objects.get(id=id)
        patient.delete()
        return 201, {"detail": "Paciente excluido com sucesso"}
    except Patient.DoesNotExist:
        return 404, {"detail": "Paciente não encontrado"}
    