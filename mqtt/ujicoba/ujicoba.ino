#if (defined(__AVR__))
#include <avr\pgmspace.h>
#else
#include <pgmspace.h>
#endif

#include <ESP8266WiFi.h>
#include <Wire.h>
#include <PubSubClient.h>

#define wifi_ssid "Pi3-AP"
#define wifi_password "raspberry"

#define mqtt_server "172.24.1.1"
#define mqtt_user ""
#define mqtt_password ""

#define topic "client"
#define uuid "7ab27738-0346-460f-a516-ec98a5d923b2"

#define BTN     D0
#define SWITCH  D5
#define LED_R   D6
#define LED_G   D7
#define LED_B   D8

int isOn = 0, lastIsOn = 0;
char payload[64];

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(9600);
  pinMode(BTN, INPUT_PULLUP);
  pinMode(SWITCH, OUTPUT);
  pinMode(LED_R, OUTPUT);
  pinMode(LED_G, OUTPUT);
  pinMode(LED_B, OUTPUT);

  setLED(1,0,0);  

  setup_wifi();
  client.setServer(mqtt_server, 1883);
}

void setup_wifi() {
  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(wifi_ssid);

  WiFi.begin(wifi_ssid, wifi_password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    // If you do not want to use a username and password, change next line to
    // if (client.connect("ESP8266Client")) {
    if (client.connect("ESP8266Client")) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setLED(int R, int G, int B){
  digitalWrite(LED_R, R);
  digitalWrite(LED_G, G);
  digitalWrite(LED_B, B);
}

double readArus(){
  return abs((((analogRead(A0)/1024.0)*5000) - 2500)/100);
}

void readStatus(){

  if(!digitalRead(BTN)){ 
    lastIsOn = isOn;
    isOn ^= 1; //XOR logic
    digitalWrite(SWITCH, isOn);
//    delay(250);
  }
  //Serial.println(isOn);
  sprintf(payload, "%s,%d,%f", uuid, isOn, readArus());
//  sprintf(payload, "%d", isOn);
//  sprintf(payload, "%f", readArus());

  Serial.println(payload);
  client.publish(topic, payload, true);
// uuid,status,daya
// 7ab27738-0346-460f-a516-ec98a5d923b2,1,0.4
//  Serial.println(status);
}

void loop() {  
  if (!client.connected()) {
    reconnect();
  }
  readStatus();  
  delay(250);
  client.loop();
}
