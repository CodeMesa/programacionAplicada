import time 
from machine import Pin 
led = Pin(2,Pin.OUT)
b=0
while b<5 :
  led.value(0.2)
  time.sleep(1)
  led.value(0)
  time.sleep(0.1)
  b=b+1
