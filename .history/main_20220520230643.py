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
def get_api_info()->AppInfo:
    json_info = json.loads(open('/assets/app_info.json').read())
    app_info = AppInfo().parse_obj(json_info)
    return app_info

