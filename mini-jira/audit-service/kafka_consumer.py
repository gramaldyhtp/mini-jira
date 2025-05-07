from kafka import KafkaConsumer
import json
from mongo import save_audit_log

def start_consumer():
    consumer = KafkaConsumer(
        'user-activity',
        bootstrap_servers='kafka:9092',
        group_id='audit-group',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    print("Audit consumer is listening on topic 'user-activity'...")

    for message in consumer:
        print(f"Received user activity: {message.value}")
        process_audit(message.value)

def process_audit(data):
    save_audit_log(data)
