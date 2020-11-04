from machine import ADC,SPI,PWM,Pin
import time, network
import neopixel,dht,BlynkLib

sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("colombo0718", "12345678")


while not sta_if.isconnected():
    pass
print('wifi connect')

token="s8UalOzfOY-Cex91g8gZdgFPcgaYc7_2"
blynk=BlynkLib.Blynk(token)

# RGB D5
np = neopixel.NeoPixel(Pin(14),1)

# light A0
light = ADC(0)


def v4_handler(value):
    print(value)
    if value[0]=='0' :
        np[0] = (0,0,0)
        np.write()
    else :
        np[0] = (10,10,10)
        np.write()
    
blynk.on("V4",v4_handler)

while True :
    blynk.run()
