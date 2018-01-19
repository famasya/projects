#if (defined(__AVR__))
#include <avr\pgmspace.h>
#else
#include <pgmspace.h>
#endif

#include <Wire.h> 
//#include <RtcDS3231.h>
//RtcDS3231<TwoWire> Rtc(Wire);

#define BTN     D0
#define SWITCH  D5
#define LED_R   D6
#define LED_G   D7
#define LED_B   D8

int isOn = 0, lastIsOn = 0;

void setLED(int R, int G, int B){
  digitalWrite(LED_R, R);
  digitalWrite(LED_G, G);
  digitalWrite(LED_B, B);
}

double readArus(){
  return ((((analogRead(A0)/1024.0)*5000) - 2500)/100);
}

void setup() {
  Serial.begin(9600);
  //Rtc.Begin();
  pinMode(BTN, INPUT_PULLUP);
  pinMode(SWITCH, OUTPUT);
  pinMode(LED_R, OUTPUT);
  pinMode(LED_G, OUTPUT);
  pinMode(LED_B, OUTPUT);

  setLED(1,0,0);  
}

void loop() {
//  RtcDateTime now = Rtc.GetDateTime();

  if(!digitalRead(BTN)){ 
    lastIsOn = isOn;
    isOn ^= 1; //XOR logic
    digitalWrite(SWITCH, isOn);
    delay(250);
  }
  
  Serial.println(isOn);
  delay(100);
}
