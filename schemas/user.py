def userEntity(item) -> dict:
    return {
        "id" : data["id"],
        "name": data["name"],
        "email": data["email"],
        "password": data["password"]
    }

def usersEntity(entity) -> list:
    [userEntity(item) for item in entity ]
    