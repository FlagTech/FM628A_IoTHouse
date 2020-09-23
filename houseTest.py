from machine import ADC,SPI,PWM,Pin
import time
import neopixel,dht

# temp
temp= dht.DHT11(Pin(16))
print(temp)

# buzzer
buzz = PWM(Pin(15))
buzz.freq(988)
buzz.duty(0)

# fan
fan=Pin(4,Pin.OUT)
fan.value(1)

# servo
servo = PWM(Pin(5), freq=50)
servo.duty(30)#舵机角度的设定

# RGB
np = neopixel.NeoPixel(Pin(14),1)
np[0] = (1,1,1)
np.write()

# laser
laser=Pin(12,Pin.OUT)
laser.value(1)

# light
light = ADC(0)

# door
door=Pin(0,Pin.IN)

# window
window=Pin(2,Pin.IN)

# sound
sound=Pin(13,Pin.IN)

# temp.measure()


while True:
    try:
        temp.measure()
    except OSError as e:
        print("can't get temp")
    print(light.read(),temp.temperature(),temp.humidity(),door.value(),window.value(),sound.value())
    
    fan.value(1)
    laser.value(1)
    servo.duty(30)
    np[0] = (1,1,1)
    np.write()
    buzz.duty(0)
    time.sleep(3)
    
    try:
        temp.measure()
    except OSError as e:
        print("can't get temp")
    print(light.read(),temp.temperature(),temp.humidity(),door.value(),window.value(),sound.value())
    
    fan.value(0)
    laser.value(0)
    servo.duty(100)
    np[0] = (0,0,0)
    np.write()
    buzz.duty(0)
    time.sleep(3)
    
    
    