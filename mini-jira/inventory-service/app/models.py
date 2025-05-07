# Struktur data untuk inventory
def format_inventory_item(item):
    return {
        "item_id": item.get("item_id"),
        "name": item.get("name"),
        "stock": item.get("stock"),
        "updated_at": item.get("updated_at")
    }
