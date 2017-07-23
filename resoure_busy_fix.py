#This should cure most "Resource busy" issues for newbies...
'''the driver should be detached
like this:
if dev.is_kernel_driver_active(0):
    reattach = True
    dev.detach_kernel_driver(0)
'''


for cfg in device:
    for intf in cfg:
        if device.is_kernel_driver_active(intf.bInterfaceNumber):
            try:
                device.detach_kernel_driver(intf.bInterfaceNumber)
            except usb.core.USBError as e:
                sys.exit("Could not detatch kernel driver from interface({0}): {1}".format(intf.bInterfaceNumber, str(e)))