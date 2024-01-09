from django.db import models
from apps.patient.models import Patient
from apps.exam.models import Exam

# Create your models here.
class Schedulling(models.Model):
    patient = models.ForeignKey(Patient)
    exam = models.ForeignKey(Exam)
    status = models.CharField()
    scheduled_to = models.DateField()
    created_at = models.DateTimeField(
        'Criado em',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Atualizado em',
        auto_now=True
    )