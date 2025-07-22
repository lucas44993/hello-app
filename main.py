from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/")
async def root():
    return {"message": f"Hello from CI/CD with ArgoCD! Updated at {datetime.datetime.now()}"}