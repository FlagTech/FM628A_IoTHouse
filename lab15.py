import ESP8266WebServer
import network,time
from machine import Pin,PWM
from umqtt.robust import MQTTClient
from rtttl import RTTTL

buzzer = PWM(Pin(15))
buzzer.duty(0)

def play_tone(freq, msec):
    if freq > 0:
        buzzer.freq(freq)   # Set frequency
        buzzer.duty(10)# 50% duty cycle
        time.sleep(msec*0.001)  # Play for a number of msec
    buzzer.duty(0)          # Stop playing
    time.sleep(0.05)
    
tune = RTTTL("Moonheart:d=4,o=5,b=140:c.,8e,g.,8c,b.4,8e,g.,8g,a.,8b,c.6,8a,2g,8e,8d,c.,8c,8c,8p,8e,8d,c.,8c,8c,8p,8d,8e,d.,8a4,b.4,16c,16d,2c")
tune = RTTTL("mario:d=4,o=5,b=100:16e6,16e6,32p,8e6,16c6,8e6,8g6,8p,8g,8p,8c6,16p,8g,16p,8e,16p,8a,8b,16a#,8a,16g.,16e6,16g6,8a6,16f6,8g6,8e6,16c6,16d6,8b,16p,8c6,16p,8g,16p,8e,16p,8a,8b,16a#,8a,16g.,16e6,16g6,8a6,16f6,8g6,8e6,16c6,16d6,8b,8p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16g#,16a,16c6,16p,16a,16c6,16d6,8p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16c7,16p,16c7,16c7,p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16g#,16a,16c6,16p,16a,16c6,16d6,8p,16d#6,8p,16d6,8p,16c6")
# for freq, msec in tune.notes():
#     play_tone(freq, msec) 


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

print(sta_if.ifconfig()[0]+"/www/lab15.html")

client = MQTTClient(
    client_id="emotion_recog", 
    server="io.adafruit.com", 
    user="AIO 帳號", 
    password="AIO 金鑰",
    ssl=False)
    
def get_cmd(topic, msg):
    print(topic,msg)
    if msg == b"60":
        print('play music')
        buzzer.duty(10)
        for freq, msec in tune.notes():
            play_tone(freq, msec) 
        buzzer.duty(0)
    else:
        buzzer.duty(0)
        
client.connect()
client.set_callback(get_cmd)
client.subscribe(b"colombo0718/feeds/emotion");

try:
    while True:
        ESP8266WebServer.handleClient()
        client.check_msg()
except:
    ESP8266WebServer.close()



