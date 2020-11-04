from machine import ADC,SPI,PWM,Pin
import time,network
import BlynkLib

sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("colombo0718", "12345678")
while not sta_if.isconnected():
    pass
print('wifi connect')

token="s8UalOzfOY-Cex91g8gZdgFPcgaYc7_2"
blynk=BlynkLib.Blynk(token)

# sound D7
sound=Pin(4,Pin.IN)

count=0
while True :
    if sound.value()==0 :
        count+=1
    if sound.value()==1 :
        count=0
        
    if count==5 :
        print('嬰兒房有聲響，快去查看')
        blynk.notify("外面有人喔")
        count=0
            
    print(sound.value(),count)
    time.sleep(.2)

