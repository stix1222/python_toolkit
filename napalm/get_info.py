from napalm import get_network_driver
from pprint import pprint
from termcolor import colored
driver = get_network_driver('ios')

with driver('192.168.1.245','case','cisco') as device:
    print(colored("-------- Get Facts --------", "red"))
    pprint(device.get_facts())
    print(colored("-------- Get Interfaces --------", "green"))
    pprint(device.get_interfaces())
    print(colored("-------- Get Arp Table ---------", "blue"))
    pprint(device.get_arp_table())
