from fastapi import FastAPI, Request
from decouple import config
from fastapi.middleware.cors import CORSMiddleware
from database import engine, get_db
import model
from router import users, auth_user


# Application initilization
app = FastAPI(title="Chain-goats", version="1.0.0")

app.include_router(users.router)
app.include_router(auth_user.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],                   
)