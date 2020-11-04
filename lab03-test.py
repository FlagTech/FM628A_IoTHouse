from machine import Pin
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

door=Pin(2,Pin.IN)

while True :
    print(door.value())
    if door.value() == 0 :
        print('有人按門鈴')
        blynk.notify("有人按門鈴")
    time.sleep(1)