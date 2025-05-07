from fastapi import FastAPI
from kafka_consumer import start_kafka_consumer

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("Starting Kafka consumer...")
    start_kafka_consumer()

@app.get("/")
def read_root():
    return {"message": "Payment Service is running"}
