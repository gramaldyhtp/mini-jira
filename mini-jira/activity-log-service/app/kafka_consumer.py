from kafka import KafkaConsumer
import json
from mongo import save_log

def consume_messages():
    consumer = KafkaConsumer(
        "activity_logs",
        bootstrap_servers="kafka:9092",
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
        group_id="activity-log-group"
    )

    print("Listening for activity logs...")
    for message in consumer:
        log_data = message.value
        print(f"Received log: {log_data}")
        save_log(log_data)
