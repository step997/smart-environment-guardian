import json #将字典字符串变为py字典
import sys  #读取别处数据，管道
from datetime import datetime   #处理时间

CSV_FILE = "sensor_data.csv" #文件名

with open(CSV_FILE, "w", encoding = "utf-8") as f:
    f.write("timestamp,temp,humi\n")

print("数据接收器已启动，等待传感器数据...")


for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    try:
        data = json.loads(line)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(CSV_FILE, "a", encoding="utf-8") as f:
            f.write(f"{now},{data['temp']},{data['humi']}\n")

        print(f"[{now}] 已记录 -> 温度：{data['temp']}℃, 湿度：{data['humi']}%")

    except json.JSONDecodeError:
        print(f"忽略无效数据：{line}")