#raspberry usb command bit fixer
#python2.x as well as 3.x

wValue = 0b0			#clear at start
r_1511 = 0b0000			#constans
r_1511 <<= 11
enumTimeout = 0b111		#variable
enumTimeout <<= 8
r_7 = 0b0				#constans
r_7 <<= 7
roleSwType = 0b10		#constans
roleSwType <<= 5
roleSwState = 0b1		#variable
roleSwState <<= 4
port = 0b1111			#variable

wValue |= r_1511 | enumTimeout | r_7 | roleSwType | roleSwState | port
print(bin(wValue))
print(hex(wValue))

input("\nenter to exit... ")

