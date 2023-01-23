from fastapi import FastAPI, Request
from decouple import config
from fastapi.middleware.cors import CORSMiddleware


# Application initilization
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],                   
)