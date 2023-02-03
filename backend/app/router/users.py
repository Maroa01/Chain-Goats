from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from schemas import schema
from utils import validator, services
import database
from typing import List
from utils.auth import get_current_active_superuser, get_current_active_user

router = APIRouter(tags=['Users'], prefix='/user')


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(request: schema.User, db: Session = Depends(database.get_db)):

    user = await validator.verify_email(request.email, db)

    if user:
        raise HTTPException(
            status_code=400,
            detail="This email is already registered."
        )

    new_user = await services.new_user_register(request, db)

    return new_user


@router.get('/', response_model=List[schema.DisplayUser])
async def get_all_users(db: Session = Depends(database.get_db), current_user: schema.User = Depends(get_current_active_user)):
    return await services.all_user(db)


@router.get('/{user_id}', response_model=schema.DisplayUser)
async def get_user_by_id(user_id: str, db: Session = Depends(database.get_db), current_user: schema.User = Depends(get_current_active_user)):
    return await services.get_user_by_id(user_id, db)

@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_user(user_id: str, db: Session = Depends(database.get_db), current_user: schema.User = Depends( get_current_active_superuser)):
    return await services.delete_user_by_id(user_id, db)

