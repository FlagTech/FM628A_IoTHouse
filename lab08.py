from machine import ADC,SPI,PWM,Pin
import time,network 
import neopixel,dht
import urandom,BlynkLib

sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Wifi 基地台", "Wifi 密碼")
while not sta_if.isconnected():
    pass
print('wifi connect')

token="Blynk 權杖"
blynk=BlynkLib.Blynk(token)

# RGB D5
np = neopixel.NeoPixel(Pin(14),1)

r=0
g=0
b=0

def v4_handler(R_Value):
    global r
#     print(r)
    r=int(R_Value[0])
    
def v5_handler(G_Value):
    global g
    g=int(G_Value[0])

def v6_handler(B_Value):
    global b
    b=int(B_Value[0])

blynk.on("V4", v4_handler)
blynk.on("V5", v5_handler)
blynk.on("V6", v6_handler)

while True :
    blynk.run()
#     r=urandom.getrandbits(1)
#     g=urandom.getrandbits(1)
#     b=urandom.getrandbits(1)
    print(r,g,b)
    np[0] = (r,g,b)
    np.write()
#     time.sleep( 1)
