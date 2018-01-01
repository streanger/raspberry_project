#for python3.x

#my part
some_hex_string = "80ab239338b8b7a7a6c0accba3d5"
def convert_endian(hex_string, n=2):
    converted = [hex_string[i:i+n] for i in range(0, len(hex_string),n)]
    converted.reverse()
    converted = "".join(converted)
    return converted

def reorder_byte(hex_string, blen=16):
    n = (blen//8)
    converted = [hex_string[i:i+n] for i in range(0,len(hex_string),n)]
    converted = "".join([converted[i+1] + converted[i] for i in range(0,len(converted), n)])
    return converted
    
    
some = reorder_byte(some_hex_string)   
print(some_hex_string) 
print(some)    
   

   
   
   
input("enter to exit...\n")