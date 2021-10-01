from napalm import get_network_driver
import json

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'}  # cisco is enable password
ios = driver('10.1.1.10', 'u1', 'cisco', optional_args=optional_args)  # napalm uses netmiko (ssh) for cisco ios
ios.open()

output = ios.get_arp_table()
dump = json.dumps(output, sort_keys=True, indent=4)
# print(dump)
with open('arp.txt', 'w') as f:
    f.write(dump)
ios.close()
