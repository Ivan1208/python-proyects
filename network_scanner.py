import scapy.all as scapy
import subprocess
#functions
def scan(ip):
    print("                                                  THIS PROGGRAM WAS MADE BY Ivan1208 //discord -> iguana#7734")
    arp_request = scapy.ARP(pdst = ip)
    arp_request.show()
    print(arp_request.summary())
    broadcast = scapy.Ether(dst = 'ff:ff:ff:ff:ff:ff')
    broadcast.show()
    arp_request_broadcast = broadcast/arp_request
    #variables
    ansewred_list = scapy.srp(arp_request_broadcast , timeout = 1 , verbose = False)[0] #solo queremos la primera respuesta ya que es ansewred
                                           #la lista de ansewred es la siguiente(ansewred , unanswered)
    print("IP \t\t\tMAC ADDRESS\n -------------------------------------------------")
    for elements in ansewred_list:
        print(elements[1].psrc + "\t\t" + elements[1].hwsrc)
    #guardar valores psrc y hwsrc en un diccionario.
ip_for_scan = input("[+]Enter your gateway address -->")
scan(ip_for_scan+"/24")
