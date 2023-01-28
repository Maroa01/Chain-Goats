from fastapi import FastAPI, Request
from decouple import config
from fastapi.middleware.cors import CORSMiddleware
from database import engine, get_db
import model


# Application initilization
app = FastAPI(title="Chain-goats", version="1.0.0")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],                   
)