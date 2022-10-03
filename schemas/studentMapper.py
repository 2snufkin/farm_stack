from models.student import Student


def toDTO(entity) -> dict:
    return {
        "id": str(entity['_id']),
        "name": entity['name'],
        "email": entity['email_address']
    }


def toListOfDTOs(entity_list) -> list:
    list_dto = []
    for student in entity_list:
        list_dto.append(toDTO(student))
    return list_dto

