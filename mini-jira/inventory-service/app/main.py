from flask import Flask, jsonify
import threading
from .kafka_consumer import consume_inventory_updates
from .mongo import inventory_collection
from .models import format_inventory_item

app = Flask(__name__)

@app.route("/inventory", methods=["GET"])
def get_inventory():
    items = inventory_collection.find()
    return jsonify([format_inventory_item(item) for item in items]), 200

if __name__ == "__main__":
    threading.Thread(target=consume_inventory_updates, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)
