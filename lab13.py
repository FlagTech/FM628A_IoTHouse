import ESP8266WebServer
import network,time
from machine import Pin,PWM
from umqtt.robust import MQTTClient

# servo D1
servo = PWM(Pin(5), freq=50)
  
# Connect to Wi-Fi if not connected
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Wifi 基地台", "Wifi 密碼")

# Wait for connecting to Wi-Fi
while not sta_if.isconnected(): 
    pass

# set port & path
ESP8266WebServer.begin(8899)
ESP8266WebServer.setDocPath("/www")

print(sta_if.ifconfig()[0]+":8899/www/lab12.html")

client = MQTTClient(
    client_id="face_recog", 
    server="io.adafruit.com", 
    user="AIO 帳號", 
    password="AIO 金鑰",
    ssl=False)
    
def get_cmd(topic, msg):
    print(topic,msg)
    if msg == b"100":
        servo.duty(30)
        print('door open')
        
        time.sleep(5)
        servo.duty(90)
        print('door close')

client.connect()
client.set_callback(get_cmd)
client.subscribe(b"AIO 帳號/feeds/voice");


try:
    while True:
        ESP8266WebServer.handleClient()
        client.check_msg()
except:
    ESP8266WebServer.close()