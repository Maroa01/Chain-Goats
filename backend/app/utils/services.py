from model import User
from typing import List, Optional
from fastapi import HTTPException, status


async def new_user_register(request, db) -> User:
    new_user = User(name=request.name, email=request.email,
                    password=request.password)
    db.add(new_user)
    db.commit()

    return new_user


async def all_user(db) -> List[User]:
    users = db.query(User).all()
    return users


async def get_user_by_id(user_id, db) -> Optional[User]:
    user_info = db.query(User).get(user_id)
    if not user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user_info

async def delete_user_by_id(user_id, db):
    db.query(User).filter(User.id == user_id).delete()
    db.commit()
