import serial
import json
import time

# COM11 是ESP8266的串口号，波特率115200
ser = serial.Serial('COM11', 115200, timeout=10)

while True:
    try:
        line = ser.readline().decode('utf-8').strip()
        if line:
            print(json.loads(line))  # 测试用，先看数据
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(1)