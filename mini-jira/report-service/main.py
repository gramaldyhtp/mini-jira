from fastapi import FastAPI
from kafka_consumer import start_consumer

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("Starting Kafka consumer for report service...")
    start_consumer()

@app.get("/")
def health_check():
    return {"message": "Report Service is running"}
