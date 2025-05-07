from kafka import KafkaConsumer
import json
from .mongo import inventory_collection
from datetime import datetime

def consume_inventory_updates():
    consumer = KafkaConsumer(
        'inventory-topic',
        bootstrap_servers='kafka:9092',
        group_id='inventory-group',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    for message in consumer:
        data = message.value
        inventory_collection.update_one(
            {"item_id": data["item_id"]},
            {"$set": {
                "name": data["name"],
                "stock": data["stock"],
                "updated_at": datetime.utcnow()
            }},
            upsert=True
        )
