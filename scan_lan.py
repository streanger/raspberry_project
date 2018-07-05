#!/usr/bin/python3
#script should check if you're in local network
#than run arp_scanning
#and finally write it to file
import subprocess

def script_path():
    print(42)
    return True

def simple_write(file, strContent):
    print(42)
    return True

def arp_scan():
    hosts = subprocess.getoutput(["arp-scan -l"])
    return hosts

def check_lan_connection():
    return True

def main():
    hosts = arp_scan()
    print(hosts)

if __name__ == "__main__":
    main()
