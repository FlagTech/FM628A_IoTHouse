from machine import Pin
import time, network, urequests

sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Wifi基地台", "Wifi密碼")
while not sta_if.isconnected():
    pass
print('wifi connect')

door=Pin(2,Pin.IN)

while True :
    print(door.value())
    if door.value() == 0 :
        print('有人按門鈴')
        urequests.get("IFTTT的HTTP請求網址")
    time.sleep(1)