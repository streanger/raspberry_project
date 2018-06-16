#from gpiozero import InputDevice, OutputDevice
import gpiozero
from time import sleep

def read_out():
    start = gpiozero.OutputDevice(23)
    #start.on()
    #sleep(0.020)
    start.off()
    sleep(0.005)
    #start.on()
    start.close()
    sensor = gpiozero.InputDevice(23, False)
    print(dir(sensor))
    data = []
    for x in range(500):
        #atime = sensor.active_time
        #itime = sensor.inactive_time
        if sensor.value:
            data.append(1)
        else:
            data.append(0)
        #print(x, atime, itime, sensor.is_active)
        #data.append(sensor.value)
        #print(x, "|", sensor.is_active)
        #sleep(0.000001)
    sensor.close()
    return data

data = read_out()
print(data)
