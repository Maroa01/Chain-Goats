from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from schemas import schema
from utils import validator, services
import database


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
