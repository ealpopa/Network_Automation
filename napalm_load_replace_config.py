from napalm import get_network_driver
import json

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'}  # cisco is enable password
ios = driver('10.1.1.10', 'u1', 'cisco', optional_args=optional_args)  # napalm uses netmiko (ssh) for cisco ios
ios.open()

ios.load_replace_candidate(filename='config.txt')
dif = ios.compare_config()
if len(dif):
    print(dif)
    ios.commit_config()
    print('Done')
else:
    print('No changes')
    ios.discard_config()

ios.close()
