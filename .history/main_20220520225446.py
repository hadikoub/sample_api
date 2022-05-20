from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get('/api/v1/health')
def hello()->str:
    return {"message": "Hello World from Dockerized FastAPI"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6000)