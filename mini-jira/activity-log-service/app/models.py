def validate_log(data):
    required_keys = {"service", "action", "timestamp", "details"}
    return all(k in data for k in required_keys)
