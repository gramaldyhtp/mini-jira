from kafka import KafkaConsumer
import json
from mongo import save_payment_log

def start_kafka_consumer():
    consumer = KafkaConsumer(
        'task-payment',
        bootstrap_servers='kafka:9092',
        group_id='payment-group',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )
    print("Kafka consumer listening on 'task-payment'...")

    for message in consumer:
        print(f"Received message: {message.value}")
        process_payment_event(message.value)

def process_payment_event(data):
    # Simulasi proses pembayaran
    print(f"Processing payment for task: {data.get('task_id')}")
    payment_result = {
        "task_id": data.get("task_id"),
        "user_id": data.get("user_id"),
        "amount": data.get("amount"),
        "status": "PAID"
    }
    save_payment_log(payment_result)
