from django.db import models
from datetime import datetime
import uuid

# Create your models here.
class Patient(models.Model):
    SEX_CHOICES=(
        ('M', 'MASCULINO'),
        ('F', 'FEMININO'),
        ('O', 'OUTROS'),
    )

    name = models.CharField(
        'Nome',
        max_length=250,
        null=False,
        blank=False
    )
    cpf = models.CharField(
        'CPF',
        max_length=14,
        null=True,
        blank=True
    )
    birth = models.DateField(
        'Nascimento',
        null=True,
        blank=True
    )
    gender = models.CharField(
        'Sexo',
        max_length=1,
        choices=SEX_CHOICES
    )
    patient_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    
    def __str__(self):
        return self.name
    
    def calculate_age(self):
        if self.birth:
            data_atual = datetime.now().date()
            idade = data_atual.year - self.birth.year - ((data_atual.month, data_atual.day) < (self.birth.month, self.birth.day))
            return idade
        return None