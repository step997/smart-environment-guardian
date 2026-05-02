import json
import time
import random

while True:
    data = {
        "temp": round(25 + random.uniform(-2, 3), 1),
        "humi": round(65 + random.uniform(-5, 5), 1)
    }
    print(json.dumps(data), flush=True)
    time.sleep(5)