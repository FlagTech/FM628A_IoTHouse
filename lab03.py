from machine import Pin
import time, network
import BlynkLib

sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Wifi 基地台", "Wifi 密碼")


while not sta_if.isconnected():
    pass
print('wifi connect')

token="Blynk 權杖"
blynk=BlynkLib.Blynk(token)

# door D4
door=Pin(2,Pin.IN)

while True :
    print(door.value())
    if door.value() == 0 :
        print('有人按門鈴')
        blynk.notify("有人按門鈴")
    time.sleep(1)