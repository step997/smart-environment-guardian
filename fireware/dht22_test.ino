#include <DHT.h>

#define DHTPIN D4
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
}

void loop() {
  delay(5000);
  
  float temp = dht.readTemperature();
  float humi = dht.readHumidity();
  
  if (isnan(temp) || isnan(humi)) {
    Serial.println("{\"error\": \"传感器读取失败\"}");
    return;
  }
  
  Serial.print("{\"temp\":");
  Serial.print(temp, 1);
  Serial.print(",\"humi\":");
  Serial.print(humi, 1);
  Serial.println("}");
}