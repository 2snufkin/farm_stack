from repo import  studentRepo


def get_all():
    return list(studentRepo.get_all())


def save_student(student):
    return studentRepo.save_one(student)



def delete_student(id):
    return studentRepo.delete_student(id)


delete_student('6339e1474e6903cb053e5dde')