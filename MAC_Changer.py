import subprocess
import optparse
import re
parser = optparse.OptionParser() 

print("MAC_CHANGER STARTED ...")
interface = ''
mac_address = ''
def get_inputs():
    parser.add_option('-i', '--interface', dest = "interface" , help = 'Interface')
    parser.add_option('-m', '--m', dest = "mac_address" , help = 'Mac address')
    (user_inputs, args) = parser.parse_args()
    return parser.parse_args()

def control_inputs(interface, mac_address):
    if not interface:
        interface = input("Enter interface: ")
    if not mac_address:
        mac_address = input("Enter mac address: ")
    return interface, mac_address

def mac_changer(interface, mac_address):
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', mac_address])
    subprocess.call(['ifconfig', interface, 'up'])

def mac_checker(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface] )
    ifconfig_str = ifconfig.decode()
    new_mac = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_str)
    if new_mac:
        return new_mac.group(0)
    else:
        return False

print('''
           __       __   ______    ______          ______   __                                                         
|  \     /  \ /      \  /      \        /      \ |  \                                                        
| $$\   /  $$|  $$$$$$\|  $$$$$$\      |  $$$$$$\| $$____    ______   _______    ______    ______    ______  
| $$$\ /  $$$| $$__| $$| $$   \$$      | $$   \$$| $$    \  |      \ |       \  /      \  /      \  /      \ 
| $$$$\  $$$$| $$    $$| $$            | $$      | $$$$$$$\  \$$$$$$\| $$$$$$$\|  $$$$$$\|  $$$$$$\|  $$$$$$\
| $$\$$ $$ $$| $$$$$$$$| $$   __       | $$   __ | $$  | $$ /      $$| $$  | $$| $$  | $$| $$    $$| $$   \$$
| $$ \$$$| $$| $$  | $$| $$__/  \      | $$__/  \| $$  | $$|  $$$$$$$| $$  | $$| $$__| $$| $$$$$$$$| $$      
| $$  \$ | $$| $$  | $$ \$$    $$       \$$    $$| $$  | $$ \$$    $$| $$  | $$ \$$    $$ \$$     \| $$      
 \$$      \$$ \$$   \$$  \$$$$$$         \$$$$$$  \$$   \$$  \$$$$$$$ \$$   \$$ _\$$$$$$$  \$$$$$$$ \$$      
                                                                               |  \__| $$                    
                                                                                \$$    $$                    
                                                                                 \$$$$$$                     

 
                                                                           by Banuchichak   ''')

(user_inputs, args) = get_inputs()
interface, mac_address=control_inputs(user_inputs.interface, user_inputs.mac_address)
mac_changer(interface,mac_address)
final_mac = mac_checker(interface)
if final_mac == mac_address:
    print("Success")
else:
    print("Unsuccess")
