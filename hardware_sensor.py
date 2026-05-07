import serial
import json
import time
from datetime import datetime

CSV_FILE = "sensor_data.csv"
ser = serial.Serial('COM11', 115200, timeout=10)

# 初始化表头
with open(CSV_FILE, "w", encoding="utf-8") as f:
    f.write("timestamp,temp,humi\n")

while True:
    try:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if line and line.startswith('{'):
            data = json.loads(line)
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            with open(CSV_FILE, "a", encoding="utf-8") as f:
                f.write(f"{now},{data['temp']},{data['humi']}\n")
            
            print(f"[{now}] 已记录真实数据 → 温度:{data['temp']}°C 湿度:{data['humi']}%")
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(1)