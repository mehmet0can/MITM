from sacpy.all import *

def get_packet_data(packet):
    print(packet.summary())

sniff(iface="eth0", prn=get_packet_data , store=0)