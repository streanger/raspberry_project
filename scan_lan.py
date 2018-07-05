#!/usr/bin/python3
#script should check if you're in local network
#than run arp_scanning
#and finally write it to file
import subprocess
import os
import sys

def script_path():
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    return path

def simple_write(file, strContent):
    with open(file, "w") as f:
        f.write(strContent + "\n")
        f.close()
    return True

def arp_scan():
    hosts = subprocess.getoutput(["arp-scan -l"])
    return hosts

def check_lan_connection():
    #t_end = time.time() + 30    #number of seconds
    #while time.time() < t_end:
    #    #check if your in lan
    #    pass
    hostname = "localhost"
    response = subprocess.getoutput(["ping -c 1 " + hostname])
    return True

def main():
    path = script_path()
    hosts = arp_scan()
    simple_write("hosts.txt", hosts)

if __name__ == "__main__":
    #check_lan_connection()
    main()
