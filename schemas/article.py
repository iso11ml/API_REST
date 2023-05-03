def articleEntity(item) -> dict:
    return {
        "title": item["title"],
        "description": item["description"],
        "date": item["date"],
        "user_id": str(item["user_id"])   # Convertir el ID del usuario a una cadena para que sea legible en la respuesta
    }

def articlesEntity(entity) -> list:
    return [articleEntity(item) for item in entity ]