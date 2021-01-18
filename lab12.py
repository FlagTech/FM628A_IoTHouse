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
ESP8266WebServer.begin(80)
ESP8266WebServer.setDocPath("/www")

print(sta_if.ifconfig()[0]+"/www/lab12.html")


try:
    while True:
        ESP8266WebServer.handleClient()
#         client.check_msg()
except:
    ESP8266WebServer.close()


