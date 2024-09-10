#include <Arduino.h>

#include "avr8-stub.h"
#include "app_api.h" //Only needed for flash breakpoints


int x=0;

void setup() {
  // put your setup code here, to run once:
  debug_init();   // debug del código en físico
  pinMode(13,OUTPUT);
}

void loop() {

  x++;

  // put your main code here, to run repeatedly:
  digitalWrite(13,LOW);
  delay(1500);
  digitalWrite(13,HIGH);
  delay(1500);
}

