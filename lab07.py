from machine import ADC,SPI,PWM,Pin
import time,dht

# fan D3 
fan=Pin(0,Pin.OUT)
fan.value(1)

# temp D7
temp = dht.DHT11(Pin(13))

while True :
    try:
        temp.measure()
        print('濕度',temp.humidity())
        
        if temp.humidity()>0:
            fan.value(1)
        else :
            fan.value(0)
    except OSError as e:
        print("尚未更新溫濕度")
        
    time.sleep(1)