import ESP8266WebServer
import network,time
from machine import Pin,PWM
from umqtt.robust import MQTTClient
from rtttl import RTTTL

# buzzer D8 
buzzer = PWM(Pin(15))
buzzer.duty(0)

tune = RTTTL("mario:d=4,o=4,b=100:16e5,16e5,32p,8e5,16c5,8e5,8g5,8p,8g,8p,8c5,16p,8g,16p,8e,16p,8a,8b,16a#,8a,16g.,16e5,16g5,8a5,16f5,8g5,8e5,16c5,16d5,8b,16p,8c5")

def play_tone(freq, msec):
    if freq > 0:
        buzzer.freq(freq)   # Set frequency
        buzzer.duty(10)# 50% duty cycle
        time.sleep(msec*0.001)  # Play for a number of msec
    buzzer.duty(0)          # Stop playing
    time.sleep(0.05)
  
# Connect to Wi-Fi if not connected
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Wifi 基地台", "Wifi 密碼")
# Wait for connecting to Wi-Fi
while not sta_if.isconnected(): 
    pass

# set port & path
ESP8266WebServer.begin(80)
ESP8266WebServer.setDocPath("/www")

print(sta_if.ifconfig()[0]+"/www/lab16.html")

client = MQTTClient(
    client_id="voice_recog", 
    server="io.adafruit.com", 
    user="AIO 帳號", 
    password="AIO 金鑰",
    ssl=False)
    
def get_cmd(topic, msg):
    print(topic,msg)
    if msg == b"100":
        print('play music')
        for freq, msec in tune.notes():
            play_tone(freq, msec) 

client.connect()
client.set_callback(get_cmd)
client.subscribe(b"AIO 帳號/feeds/voice");

try:
    while True:
        ESP8266WebServer.handleClient()
        client.check_msg()
except:
    ESP8266WebServer.close()



