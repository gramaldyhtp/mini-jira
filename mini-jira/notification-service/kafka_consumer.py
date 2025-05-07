from kafka import KafkaConsumer
import json
from mongo import save_notification_log

def start_consumer():
    consumer = KafkaConsumer(
        'task-updated',
        bootstrap_servers='kafka:9092',
        group_id='notification-group',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    print("Notification consumer is listening on topic 'task-updated'...")

    for message in consumer:
        print(f"Received message: {message.value}")
        process_notification(message.value)

def process_notification(data):
    notification = {
        "user_id": data.get("user_id"),
        "task_id": data.get("task_id"),
        "message": f"Task '{data.get('title')}' has been updated",
        "status": "sent"
    }
    save_notification_log(notification)
