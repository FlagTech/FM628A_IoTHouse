from machine import ADC,SPI,PWM,Pin
import time
import neopixel,dht

# fan D3 
fan=Pin(0,Pin.OUT)
fan.value(1)