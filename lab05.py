import time, network, urequests
import BlynkLib

sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("colombo0718", "12345678")

while not sta_if.isconnected():
    pass
print('wifi connect')

token="s8UalOzfOY-Cex91g8gZdgFPcgaYc7_2"
blynk=BlynkLib.Blynk(token)

def v1_handler():
    res= urequests.get("http://api.waqi.info/feed/taiwan/shihlin/?token=d08147c688ce823984d8a42281bdc01f7e3c3a53")
    j=res.json()
    print(j['data']['city']['name'],j['data']['aqi'])
    blynk.virtual_write(1,j['data']['aqi'])

blynk.on("readV1",v1_handler)

while True :
    blynk.run()
    