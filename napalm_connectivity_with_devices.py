from napalm import get_network_driver
import json

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'}  # cisco is enable password
ios = driver('10.1.1.10', 'u1', 'cisco', optional_args=optional_args)  # napalm uses netmiko (ssh) for cisco ios
ios.open()

output = ios.ping(destination='10.1.1.20', count=2)
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

ios.close()
