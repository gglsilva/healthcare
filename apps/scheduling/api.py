from ninja import Router
from datetime import date
from .models import Scheduling
from apps.patient.models import Patient
from apps.exam.models import Exam
from .schema import SchedulingSchema, NotFoundResponse
from django.shortcuts import get_object_or_404

router = Router()

# CRUD
@router.get('/{id}', tags=["SCHEDULING"])
def read(request, id:int):
    try:
        schedule = get_object_or_404(Scheduling, id=id)
        return schedule
    except Exception:
        return 404, {"detail": "Paciente não encontrado"}
   

@router.post('/', tags=["SCHEDULING"])
def create(request, schedule: SchedulingSchema):
    new_schedule = schedule.dict()
    try:
        patient = get_object_or_404(Patient, id=new_schedule['patient'])
        exam = get_object_or_404(Exam, id=new_schedule['exam'])
        schedule = Scheduling.objects.create(
            patient=patient,
            exam=exam,
            preference=schedule.preference,
            status=schedule.status,
            scheduled_to=schedule.scheduled_to,
            created_at=schedule.created_at,
            updated_at=schedule.updated_at
        )
        schedule.save()

        return 200, {'detail': 'Agendamento criado com sucesso'}

    except Exception:
        return 400, {"detail": "Falha ao tentar Criar um novo agendamento"}


@router.put('/{schedule_id}', tags=["SCHEDULING"])
def update_schedule(request, schedule_id: int, schedule: SchedulingSchema):
    try:
        # Obtém o agendamento existente pelo ID
        existing_schedule = get_object_or_404(Scheduling, id=schedule_id)

        # Obtém os objetos do paciente e do exame se forem alterados na atualização
        patient = get_object_or_404(Patient, id=schedule.patient)
        exam = get_object_or_404(Exam, id=schedule.exam)

        # Atualiza os campos do agendamento existente
        existing_schedule.patient = patient
        existing_schedule.exam = exam
        existing_schedule.preference = schedule.preference
        existing_schedule.status = schedule.status
        existing_schedule.scheduled_to = schedule.scheduled_to
        existing_schedule.created_at = schedule.created_at
        existing_schedule.updated_at = schedule.updated_at

        existing_schedule.save()

        return 200, {'detail': 'Agendamento atualizado com sucesso'}

    except Scheduling.DoesNotExist:
        return 404, {'detail': 'Agendamento não encontrado'}
    except Exception:
        return 400, {'detail': 'Falha ao tentar atualizar o agendamento'}


@router.delete("/{id}", tags=["SCHEDULING"], response={201: None, 404: NotFoundResponse})
def delete(request, id: int):
    try:
        schedule = Scheduling.objects.get(id=id)
        schedule.delete()
        return 201, {"detail": "Agendamento excluido com sucesso"}
    except Patient.DoesNotExist:
        return 404, {"detail": "Paciente não encontrado"}

# LISTS
    