from fastapi import APIRouter

from models.student import Student
from schemas import studentMapper
from services import studentService

student_router = APIRouter()


@student_router.get('/students')
async def find_all_students():
    all_stud =  studentService.get_all()
    return studentMapper.toListOfDTOs(all_stud)


@student_router.post('/student')
async def create_student(student: Student):
    return studentService.save_student(dict(student))

@student_router.delete('/student/{id}')
async def delete_student(id: str):
     studentService.delete_student(id)
