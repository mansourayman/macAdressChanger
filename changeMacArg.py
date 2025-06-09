#!/usr/bin/env python3
import subprocess
import argparse
import re

def changeMac(newMac, interface):
    try:
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "hw", "ether", newMac])
        subprocess.call(["ifconfig", interface, "up"])
        print(f"[+] MAC address changed to {newMac} on {interface}")
    except subprocess.CallProcessError:
        print("[-] ERROR in process")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MAC ADDRESS CHANGER")
    parser.add_argument("--interface", help="Interface card name like eth0, wlan0")
    parser.add_argument("--mac", help="Enter new MAC address")
    args = parser.parse_args()

    if not args.interface or not args.mac:
        print("[-] Please provide both --interface and --mac arguments.")
    elif not re.fullmatch(r"([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}", args.mac):
        print("[-] Invalid MAC address format. Use format like 00:11:22:33:44:55")
    else:
        changeMac(args.mac, args.interface)

