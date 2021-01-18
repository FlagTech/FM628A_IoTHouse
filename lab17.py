from machine import Pin
import time, network, urequests

sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Wifi 基地台", "Wifi 密碼")
while not sta_if.isconnected():
    pass
print('wifi connect')

# window D0
window=Pin(16,Pin.IN)

while True :
    print(window.value())
    if window.value() == 1 :
        print('家裡遭小偷，請盡速查看')
        urequests.get("IFTTT 的 HTTP 請求網址")
        time.sleep(10)
    time.sleep(1)