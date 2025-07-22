from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/")
async def root():
    return {"message": f"Hello from CI/CD with Pull Request! Current time: {datetime.datetime.now()}"}