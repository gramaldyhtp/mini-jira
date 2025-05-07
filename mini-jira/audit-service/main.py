from fastapi import FastAPI
from kafka_consumer import start_consumer

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("Starting Kafka consumer for audit service...")
    start_consumer()

@app.get("/")
def health_check():
    return {"message": "Audit Service is running"}
