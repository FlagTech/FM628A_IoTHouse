from machine import Pin
import time, network, urequests
import dht
import BlynkLib

sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Wifi 基地台", "Wifi 密碼")
while not sta_if.isconnected():
    pass
print('wifi connect')

token="Blynk 權杖"
blynk=BlynkLib.Blynk(token)

# temp D7
temp = dht.DHT11(Pin(13))

def v1_handler():
    res= urequests.get("AQI 網址")
    j=res.json()
    print(j['data']['city']['name'],'空污指數',j['data']['aqi'])
    blynk.virtual_write(1,'AQI:'+str(j['data']['aqi']))

def v2_handler():
    try:
        temp.measure()
        print('溫度 濕度',temp.temperature(),temp.humidity())
    except OSError as e:
        print("尚未更新溫濕度")
    blynk.virtual_write(2,str(temp.temperature())+' ℃')
  
def v3_handler():
    blynk.virtual_write(3,str(temp.humidity())+' %')

blynk.on("readV1",v1_handler)
blynk.on("readV2",v2_handler)
blynk.on("readV3",v3_handler)

while True :
    blynk.run()
    