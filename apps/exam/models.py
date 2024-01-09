from django.db import models

# Create your models here.
class Exam(models.Model):
    name = models.CharField(
        'Exame',
        max_length=255,
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(
        'Criado em',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Atualizado em',
        auto_now=True
    )
    
    def __str__(self):
        return str(self.name)