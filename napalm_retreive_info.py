from napalm import get_network_driver
import json

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'}  # cisco is enable password
ios = driver('10.1.1.10', 'u1', 'cisco', optional_args=optional_args)  # napalm uses netmiko (ssh) for cisco ios
ios.open()

# output = ios.get_facts()
# output = ios.get_arp_table()
# output = ios.get_interfaces()
# output = ios.get_users()
# output = ios.get_interfaces_counters()
# output = ios.get_interfaces_ip()
output = ios.get_config()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

# for k,v in output.items():
#     print(k, v)

ios.close()
