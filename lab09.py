from machine import ADC,SPI,PWM,Pin
import time
import neopixel,dht
import urandom

# RGB D5
np = neopixel.NeoPixel(Pin(14),1)

while True :
    r=urandom.getrandbits(10)
    g=urandom.getrandbits(10)
    b=urandom.getrandbits(10)
    np[0] = (r,g,b)
    np.write()
    time.sleep( 1)
