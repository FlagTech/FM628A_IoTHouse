from machine import ADC,SPI,PWM,Pin
import time
import neopixel,dht

# buzzer D8 
buzz = PWM(Pin(15))
buzz.freq(392)
buzz.duty(0)

# door D4
door=Pin(2,Pin.IN)

# window D0
window=Pin(16,Pin.IN)

# servo D1
servo = PWM(Pin(5), freq=50)

# temp D7
temp= dht.DHT11(Pin(13))

# fan D3 
fan=Pin(0,Pin.OUT)

# RGB D5
np = neopixel.NeoPixel(Pin(14),1)

# light A0
light = ADC(0)

# laser D6
laser=Pin(12,Pin.OUT)

# sound D2
sound=Pin(4,Pin.IN)

while True:
    try:
        temp.measure()
    except OSError as e:
        print("can't get temp")
    print("光感測  溫度  濕度  按鈕  磁簧  聲音")
    print(light.read(),temp.temperature(),temp.humidity(),door.value(),window.value(),sound.value())
#     print(light.read(),door.value(),window.value(),sound.value())

    fan.value(1)
    laser.value(1)
    servo.duty(90)
    np[0] = (10,10,10)
    np.write()
    buzz.duty(500)
    time.sleep(5)
    
    try:
        temp.measure()
    except OSError as e:
        print("can't get temp")
    print("光感測  溫度  濕度  按鈕  磁簧  聲音")
    print(light.read(),temp.temperature(),temp.humidity(),door.value(),window.value(),sound.value())
#     print(light.read(),door.value(),window.value(),sound.value())
    
    fan.value(0)
    laser.value(0)
    servo.duty(30)
    np[0] = (0,0,0)
    np.write()
    buzz.duty(0)
    time.sleep(5)
    
    
    
