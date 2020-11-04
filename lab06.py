from machine import Pin
import time, network, urequests
import dht
import BlynkLib

sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("colombo0718", "12345678")
while not sta_if.isconnected():
    pass
print('wifi connect')

token="s8UalOzfOY-Cex91g8gZdgFPcgaYc7_2"
blynk=BlynkLib.Blynk(token)

# temp D7
temp = dht.DHT11(Pin(13))

def v1_handler():
    res= urequests.get("http://api.waqi.info/feed/taiwan/shihlin/?token=d08147c688ce823984d8a42281bdc01f7e3c3a53")
    j=res.json()
    print(j['data']['city']['name'],'空污指數',j['data']['aqi'])
    blynk.virtual_write(1,j['data']['aqi'])

def v2_handler():
    try:
        temp.measure()
        print('溫度 濕度',temp.temperature(),temp.humidity())
    except OSError as e:
        print("尚未更新溫濕度")
    blynk.virtual_write(2,temp.temperature())
  
def v3_handler():
    blynk.virtual_write(3,temp.humidity())

blynk.on("readV1",v1_handler)
blynk.on("readV2",v2_handler)
blynk.on("readV3",v3_handler)

while True :
    blynk.run()
    