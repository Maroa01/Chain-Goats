from fastapi import HTTPException, status
from model import User

async def new_user_register(request,db) -> User:
    new_user = User(name=request.name, email=request.email, password=request.password)
    db.add(new_user)
    db.commit()

    return new_user