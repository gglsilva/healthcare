from ninja import Router
from .models import Exam
from .serializers import ExamSerializer, ExamResponseSerializer

router = Router()

@router.get("/", tags=["Exam"], response={200: list[ExamResponseSerializer]})
def list_exams(request):  
    """
    Retorna a lista de todos os exames.
    """
    exams = Exam.objects.all()
    
    return exams

@router.get("/{exam_id}", tags=["Exam"], response={200: ExamResponseSerializer})
def get_exam(request, exam_id: int):
    """
    Retorna detalhes de um exame específico.
    """
    exam = Exam.objects.get(id=exam_id)
    return exam

@router.post("/", tags=["Exam"], response={201: ExamResponseSerializer})
def create_exam(request, exam: ExamSerializer):
    """
    Cria um novo exame.
    """
    new_exam = Exam.objects.create(**exam.dict())
    return new_exam

@router.put("/{exam_id}", tags=["Exam"], response={200: ExamResponseSerializer})
def update_exam(request, exam_id: int, exam: ExamSerializer):
    """
    Atualiza detalhes de um exame existente.
    """
    updated_exam = Exam.objects.filter(id=exam_id).update(**exam.dict())
    return Exam.objects.get(id=exam_id)

@router.delete("/{exam_id}", tags=["Exam"], response={204: None})
def delete_exam(request, exam_id: int):
    """
    Exclui um exame existente.
    """
    Exam.objects.filter(id=exam_id).delete()
    return None
