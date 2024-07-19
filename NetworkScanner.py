import scapy.all as scapy
import optparse

def get_user_input():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--ip_address', dest='ip_address', help='IP address or range to scan')
    return parser.parse_args()

def validate_input(ip_address):
    if not ip_address:
        ip_address = input("Enter IP address: ")
    return ip_address

def scan_network(ip_address):
    arp_request = scapy.ARP(pdst = ip_address)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_request_packet = broadcast / arp_request
    answered, unanswered = scapy.srp(arp_request_packet, timeout = 1)
    answered.summary()

print('''
 /$$   /$$             /$$     /$$      /$$                     /$$              /$$$$$$                                                             
| $$$ | $$            | $$    | $$  /$ | $$                    | $$             /$$__  $$                                                            
| $$$$| $$  /$$$$$$  /$$$$$$  | $$ /$$$| $$  /$$$$$$   /$$$$$$ | $$   /$$      | $$  \__/  /$$$$$$$  /$$$$$$  /$$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$ 
| $$ $$ $$ /$$__  $$|_  $$_/  | $$/$$ $$ $$ /$$__  $$ /$$__  $$| $$  /$$/      |  $$$$$$  /$$_____/ |____  $$| $$__  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$  $$$$| $$$$$$$$  | $$    | $$$$_  $$$$| $$  \ $$| $$  \__/| $$$$$$/        \____  $$| $$        /$$$$$$$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$\  $$$| $$_____/  | $$ /$$| $$$/ \  $$$| $$  | $$| $$      | $$_  $$        /$$  \ $$| $$       /$$__  $$| $$  | $$| $$  | $$| $$_____/| $$      
| $$ \  $$|  $$$$$$$  |  $$$$/| $$/   \  $$|  $$$$$$/| $$      | $$ \  $$      |  $$$$$$/|  $$$$$$$|  $$$$$$$| $$  | $$| $$  | $$|  $$$$$$$| $$      
|__/  \__/ \_______/   \___/  |__/     \__/ \______/ |__/      |__/  \__/       \______/  \_______/ \_______/|__/  |__/|__/  |__/ \_______/|__/      
                                                                                                                                                     
                                                                                                                                                 by Banuchichak
''')
user_inputs, arg = get_user_input()
ip_address = validate_input(user_inputs.ip_address)
scan_network(ip_address)
