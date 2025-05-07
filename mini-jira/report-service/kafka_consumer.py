from kafka import KafkaConsumer
import json
from mongo import save_report_log

def start_consumer():
    consumer = KafkaConsumer(
        'task-updated',
        bootstrap_servers='kafka:9092',
        group_id='report-group',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    print("Report consumer is listening on topic 'task-updated'...")

    for message in consumer:
        print(f"Received task update for report: {message.value}")
        process_report(message.value)

def process_report(data):
    report = {
        "task_id": data.get("task_id"),
        "title": data.get("title"),
        "updated_by": data.get("updated_by"),
        "status": data.get("status"),
        "timestamp": data.get("timestamp"),
    }
    save_report_log(report)
