from machine import Pin,PWM,ADC
import time, network,dht, urequests,neopixel
import BlynkLib
from rtttl import RTTTL

sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Wifi 基地台", "Wifi 密碼")


while not sta_if.isconnected():
    pass
print('wifi connect')

token="Blynk 權杖"
blynk=BlynkLib.Blynk(token)

# buzzer D8 
buzzer = PWM(Pin(15))
buzzer.duty(0)

# tune = RTTTL("Moonheart:d=4,o=5,b=140:c.,8e,g.,8c,b.4,8e,g.,8g,a.,8b,c.6,8a,2g,8e,8d,c.,8c,8c,8p,8e,8d,c.,8c,8c,8p,8d,8e,d.,8a4,b.4,16c,16d,2c")

def play_tone(freq, msec):
    if freq > 0:
        buzzer.freq(freq)   # Set frequency
        buzzer.duty(10)# 50% duty cycle
        time.sleep(msec*0.001)  # Play for a number of msec
    buzzer.duty(0)          # Stop playing
    time.sleep(0.05)

# door D4
door=Pin(2,Pin.IN)

# servo D1
servo = PWM(Pin(5), freq=50)
servo.duty(30)

# temp D7
temp = dht.DHT11(Pin(13))

# fan D3 
fan=Pin(0,Pin.OUT)
fan.value(1)

# RGB D5
np = neopixel.NeoPixel(Pin(14),1)

r=0
g=0
b=0

# light A0
light = ADC(0)

# laser D6
laser=Pin(12,Pin.OUT)
laser.value(1)

# sound D2
sound=Pin(4,Pin.IN)

# window D0
window=Pin(16,Pin.IN)

def v0_handler(value):
    print(value[0])
    if value[0]=="0":
        servo.duty(30)
        print('大門打開')
    else :
        servo.duty(100)
        print('大門關閉')
        
def v1_handler():
    res= urequests.get("AQI 網址")
    j=res.json()
    print(j['data']['city']['name'],j['data']['aqi'])
    blynk.virtual_write(1,j['data']['aqi'])
    
def v2_handler():
    try:
        temp.measure()
        print('溫度 濕度',temp.temperature(),temp.humidity())
        if temp.humidity()>80:
            fan.value(1)
            print("濕度過高，開啟空調")
        else :
            fan.value(0)
    except :
        print("尚未更新溫濕度")
    blynk.virtual_write(2,str(temp.temperature())+' ℃')
  
def v3_handler():
    blynk.virtual_write(3,str(temp.humidity())+' %')
    
def v4_handler(R_Value):
    global r
    r=int(R_Value[0])
    
def v5_handler(G_Value):
    global g
    g=int(G_Value[0])

def v6_handler(B_Value):
    global b
    b=int(B_Value[0])

blynk.on("V0", v0_handler)
blynk.on("readV1",v1_handler)
blynk.on("readV2",v2_handler)
blynk.on("readV3",v3_handler)
blynk.on("V4", v4_handler)
blynk.on("V5", v5_handler)
blynk.on("V6", v6_handler)

count=0
while True :
    blynk.run()

    if door.value() == 0 :
        print('有人按門鈴')
        blynk.notify("有人按門鈴")
        time.sleep(5)
    
    if light.read() < 100 and laser.value()==1 :
        print("外面有人喔")
        blynk.notify("外面有人喔")
        time.sleep(5)
        
    if sound.value()==1 :
        count+=1
    if sound.value()==0 :
        count=0
    if count==5 :
        print('嬰兒房有聲響，快去查看')
        blynk.notify("嬰兒房有聲響，快去查看")
        count=0
        
    if window.value() == 1 :
        print('家裡遭小偷，請盡速查看')
        urequests.get("IFTTT 的 HTTP 請求網址")
        time.sleep(10)
        
    np[0] = (r,g,b)
    np.write()