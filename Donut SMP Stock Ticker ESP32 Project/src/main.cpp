#include <Arduino.h>
#include <WiFi.h>
#include "secrets.h"
#include <HTTPClient.h>
#include <ArduinoJson.h>

String single_item = "https://api.donut.auction/v2/items/prices?itemIds=";

unsigned long lastTime = 0;
unsigned long timerDelay = 10000;

const char* ssid = my_ssid;
const char* password = my_password;

void initWiFi() {
  WiFi.mode(WIFI_STA);
  Serial.println("mode set wifi satation");
  WiFi.begin(ssid, password);
  Serial.println("wifi beginned");
  Serial.print("Connecting to WiFi ..");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print('.');
    delay(1000);
  }
  Serial.println(WiFi.localIP());
  Serial.println("CONNECTED HELL YEAHHHHHHHHHHH");
}

void setup() {
  Serial.begin(115200);
  delay(1000);
  initWiFi();
}

void loop() {
  if ((millis() - lastTime) > timerDelay) {
    HTTPClient http;
    String elytra_url = single_item + "c4c7f62a-d21a-4e94-b6a3-355a15349705";
    http.begin(elytra_url.c_str());
    int httpResponseCode = http.GET();
    String payload = http.getString();
    Serial.println(payload);
    JsonDocument doc;
    DeserializationError error = deserializeJson(doc, payload);
    if (error) {
      Serial.print("Desearlixe failed :( : ");
      Serial.println(error.c_str());
      return;
    }
    double price = doc[0]["price"]["value"];
    Serial.println(price);
    if (price > 1000000) { 
      price = price / 1000000;
    }
    else if (price > 1000) {
      price = price / 1000;
    }
  
  Serial.print(price, 2);
  Serial.println("M");
  lastTime = millis();
  }
}
