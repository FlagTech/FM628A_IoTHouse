from machine import Pin,PWM 
import time

buzzer = PWM(Pin(15))
buzzer.duty(512)

buzzer.freq(261)
time.sleep(.5)
buzzer.freq(494)
time.sleep(.5)
buzzer.freq(261)
time.sleep(.5)
buzzer.freq(494)
time.sleep(.5)
buzzer.freq(261)
time.sleep(.5)
buzzer.freq(494)
time.sleep(.5)

buzzer.duty(0)
