#python2.7 usb finder, modified by ps

import re
import subprocess
device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
df = subprocess.check_output("lsusb")
devices = []
for i in df.split('\n'):
    if i:
        info = device_re.match(i)
        if info:
            dinfo = info.groupdict()
            dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
            devices.append(dinfo)

			
def show_devices(devices, nameTag=True):
    name = "hidden"
    for index, device in enumerate(devices):
        vidpid = (device["id"]).split(':')
        if(nameTag):
            name = device["tag"]
        print "|No.%s |Vid:%s |Pid:%s |Name:%s" % (index, vidpid[0], vidpid[1], name)
		
show_devices(devices)

raw_input("\nenter to finish... ")
