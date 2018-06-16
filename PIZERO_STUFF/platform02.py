
#this is python script for ultimate platform
#16.10.17
import gpiozero
from time import sleep

#led1 = gpiozero.LED(24)

def blink_led(speed, cycles):
    for x in range(cycles):
        accelerate = speed/(x/10+1)
        print("accelerate:",accelerate)
        led1.on()
        #print("Value:",led1.value)
        sleep(accelerate)
        led1.off()
        sleep(accelerate)

def just_blink(some_led, step=0.5):
    some_led.on()
    sleep(step)
    some_led.off()
    sleep(step)
    some_led.on()
    sleep(step)
    some_led.off()

def cpu_temp():
    temp = gpiozero.CPUTemperature()
    return temp.temperature

def dht11_run():
    pass

def buzzer_run():
    #physicaly GPIO_12
    print(42)


if __name__ == "__main__":
    #print(gpiozero.pi_info())
    #led1 = gpiozero.LED(24)
    #just_blink(led1, step=0.1)
    buzzer_run()
