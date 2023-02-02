from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status

from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import database
from utils import hashing
from model import User
from utils.auth import create_access_token

router = APIRouter(tags=['auth'])

@router.post('/login')
def login(request:OAuth2PasswordRequestForm= Depends(), db: Session = Depends(database.get_db)):
    user = db.query(User).filter(User.email ==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details='Invalid Credentials')
    
    if not hashing.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid Password')


    access_token = create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}