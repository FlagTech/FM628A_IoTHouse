import time, network, urequests
import BlynkLib

sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Wifi 基地台", "Wifi 密碼")

while not sta_if.isconnected():
    pass
print('wifi connect')

token="Blynk 權杖"
blynk=BlynkLib.Blynk(token)

def v1_handler():
    res= urequests.get("AQI 網址")
    j=res.json()
    print(j['data']['city']['name'],j['data']['aqi'])
    blynk.virtual_write(1,j['data']['aqi'])

blynk.on("readV1",v1_handler)

while True :
    blynk.run()
    