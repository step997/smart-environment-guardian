import json
import time
import random
from datetime import datetime

CSV_FILE = "sensor_data.csv"

#只在文件不存在时，写一次表头
try:
    with open(CSV_FILE, "x", encoding="utf-8") as f:
        f.write("timestamp,temp,humi\n")
except FileExistsError:
    pass #文件已存在，不动表头

while True:
    data = {
        "temp": round(25 + random.uniform(-2, 3), 1),
        "humi": round(65 + random.uniform(-5, 5), 1)
    }

    #先在屏幕上打印出来，方便观察
    print(json.dumps(data), flush=True)

    #再把数据安静地追加到 CSV 文件里
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(CSV_FILE, "a", encoding="utf-8") as f:
        f.write(f"{now},{data['temp']},{data['humi']}\n")

    time.sleep(5)