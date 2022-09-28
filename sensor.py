from sr04 import HCSR04
import time
import lightbrary
import machine


l = lightbrary.Light(180,12)
USsensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)
PIRsensor = machine.Pin(27, machine.Pin.IN)

    


while True:
    distance = USsensor.distance_cm()
    if distance > 50 or distance < 1:
        l.s_blink(l.c1, 500)
    if distance < 50 and distance > 1 or PIRsensor.value()==1:
        print (PIRsensor.value())
        print('boing')
        l.s_pulse(50,50,50)
        