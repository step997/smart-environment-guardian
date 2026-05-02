#1.搬工具
from fastapi import FastAPI     #FastAPI 框架，帮我们快速搭建网站后端
from fastapi.middleware.cors import CORSMiddleware      #解决跨域问题，让前端能请求我们

import csv      #提取 CSV 文件用
import os       #检查文件是否存在

#2.创建一个 "应用"
app = FastAPI(title="智能环境哨兵 API", version="1.0")

#3.允许任何人来访问
#   以后前端页面和API不在同一个地址时，这个配置就不会报错
app.add_middleware(
    CORSMiddleware,
    # "*" 表示允许所有来源
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"],
)

#4.定义我们的数据文件(就是虚拟传感器写的那个CSV)
CSV_FILE = "sensor_data.csv"


#5.写第一个API接口：获取最新一条数据
@app.get("/api/latest")
def get_latest():
    """
    返回 sensor_data.csv 里最后一行温湿度数据
    """
    
    #如果文件不存在，报错
    if not os.path.exists(CSV_FILE):
        return{"error": "还没有数据，请先运行传感器"}

    #打开CSV文件，读所有行
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    #如果只有表头或者空文件，说明没数据
    if len(lines) < 2:
        return {"error": "CSV 中暂无数据"}

    #取最后一行(最新数据)
    last_line = lines[-1].strip()       #.strip() 去掉换行符
    parts = last_line.split(",")        #用逗号切开：时间，温度，湿度
    #parts[0]是时间，parts[1]是温度，parts[2]是湿度
    return{
        "timestamp":parts[0],
        "temp":float(parts[1]),
        "humi":float(parts[2])
    }

#6.这个if判断：只有直接运行api_server.py时才启动服务器
#   如果被别人import, 就不启动
if __name__ == "__main__":
    import uvicorn
    #uvicorn.run 启动服务器
    #app 是我们要运行的应用
    #host = "0.0.0.0" 让同一个wifi下的其他设备也能访问
    #port = 8000 端口号
    uvicorn.run(app, host="0.0.0.0",port=8000)
