#include <WiFi.h>
#include <WiFiUdp.h>

const char* ssid = "";
const char* password = "";

const int echoPin = 18;
const int trigPin = 5;
const int udpPort = 12345;
const char* udpServerIP = "192.168.1.17";

WiFiUDP udp;

long duration;
int distance;

void setup() {
  Serial.begin(9600);
  
  connectToWiFi();
  
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  
  Serial.println("Distance measurement using JSN-SR04T");
  delay(500);

  udp.begin(udpPort);
}

void connectToWiFi() {
  WiFi.begin(ssid, password);
  Serial.print("\nConnecting");

  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(100);
  }

  Serial.println("\nConnected to the WiFi network");
  Serial.print("Local ESP32 IP: ");
  Serial.println(WiFi.localIP());
}

void measureDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);

  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.0344 / 2;
  Serial.print(distance);

}

void sendDistanceToServer() {
  udp.beginPacket(udpServerIP, udpPort);
  udp.print(distance);
  udp.endPacket();
}

void loop() {
  measureDistance();
  sendDistanceToServer();

  delay(10000);
}
