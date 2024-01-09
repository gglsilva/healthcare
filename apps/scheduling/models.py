from django.db import models
from apps.patient.models import Patient
from apps.exam.models import Exam
from .choices import *

# Create your models here.
class Scheduling(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )
    exam = models.ForeignKey(
        Exam,
       on_delete=models.CASCADE
    )
    preference = models.CharField(
        'Preferência',
        max_length=3,
        choices=PREFERENCE_CHOICES,
        null=False,
        blank=False
    )
    status = models.CharField(
        'Status',
        max_length=2,
        choices=SCHEDULE_STATUS,
        null=False,
        blank=False
    )
    scheduled_to = models.DateField()
    created_at = models.DateTimeField(
        'Criado em',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Atualizado em',
        auto_now=True
    )
    
    def __str__(self) -> str:
        return self.patient.name