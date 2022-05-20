from fastapi import FastAPI
from typing import Dict
import json
from pydantic import BaseModel

class AppInfo(BaseModel):
    name:str
    title:str
    version:int
    description:str



app = FastAPI()


@app.get('/api/v1/health')
def hello()->Dict:
    return {"message": "Hello World from Dockerized FastAPI"}


@app.get('/api/v1/info')

