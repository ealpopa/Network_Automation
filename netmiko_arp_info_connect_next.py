import netmiko
import re

cisco_device = {
    'host': '10.1.1.20',
    'port': '22',
    'username': 'u1',
    'password': 'cisco',
    'device_type': 'cisco_ios',
    'secret': 'cisco',
    'verbose': True
}

#connect to first router
with netmiko.ConnectHandler(**cisco_device) as ssh:
    # get arp table
    output = ssh.send_command('show arp')

# regex and rudimentary 4-octets testing to extract IP
ips = re.findall(r'([0-9.]*)', output)
is_ip = lambda _: len(_.split('.')) == 4

#if ip different from own IP, store in list
ips = [ip for ip in ips if is_ip(ip) and ip not in cisco_device['host']]
print('These IPs have been found in ARP table:')
print(ips)

for host in ips:
    cisco_device['host'] = host
    try:
        print(f'Trying to connect to {host}...')
        with netmiko.ConnectHandler(**cisco_device) as ssh:
            output = ssh.send_command('show run')
        print('*' * 20)
        print(f'This is the running config for {host}:')
        print('*' * 20)
        print(output)
        print('*' * 20)
        print(f'Disconnected from {host}')
    except Exception as e:
        print(e)
