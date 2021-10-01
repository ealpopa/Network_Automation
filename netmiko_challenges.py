import netmiko
import json
import threading

##
## Simple show arp table
##

device = {
    'host': '10.1.1.20',
    'port': '22',
    'username': 'u1',
    'password': 'cisco',
    'secret': 'cisco',
    'device_type': 'cisco_ios'
}

ssh = netmiko.ConnectHandler(**device)
output = ssh.send_command('show arp')
print(output)
ssh.disconnect()


##
## Simple commands send
##

device = {
    'host': '10.1.1.10',
    'port': '22',
    'username': 'u1',
    'password': 'cisco',
    'secret': 'cisco',
    'device_type': 'cisco_ios'
}

ssh = netmiko.ConnectHandler(**device)
ssh.config_mode()
ssh.send_command('username admin secret topsecret')
ssh.exit_config_mode()
ssh.send_command('terminal length 0')
config = ssh.send_command('show run')
prompt = ssh.find_prompt()
filename = f'{prompt}-running-config.txt'
with open(filename, 'w') as f:
    f.write(config)


##
## Write commands outputs in files
##


devices = []

with open('device_data.txt') as f:
    info = f.read().splitlines()
    for device in info:
        devices.append({
            'host': device.split(':')[0],
            'port': device.split(':')[1],
            'username': device.split(':')[2],
            'password': device.split(':')[3],
            'secret': device.split(':')[4],
            'device_type': 'cisco_ios'
        })
    # device_json = json.dumps(devices, indent=4)
    # print(device_json)

commands = ['terminal length 0', 'show ip int brief', 'show run', 'configure terminal']


def run(dev, cmds):
    with netmiko.ConnectHandler(**dev) as ssh:
        prompt = ssh.find_prompt()
        hostname = prompt.rstrip('#')
        # print(hostname)
        for cmd in cmds:
            output = ssh.send_command(cmd)
            filename = f'{hostname}-{cmd[:10]}' + '.txt'
            with open(filename, 'w') as f:
                f.write(prompt.rstrip('#') + '\n')
                f.write(output)


th_list = []

for device in devices:
    th = threading.Thread(target=run, args=(device,commands))
    th_list.append(th)

for i,th in enumerate(th_list):
    th.start()
    print(f'started thread {i}')

for th in th_list:
    th.join()

###
### Prompt for username and password
###

from getpass import getpass
devices = []

with open('device_data.txt') as f:
    info = f.read().splitlines()
    for device in info:
        username = input(f"Please enter username for host {device.split(':')[0]}: ")
        password = getpass(f"Please enter password for host {device.split(':')[0]}: ")
        devices.append({
            'host': device.split(':')[0],
            'port': device.split(':')[1],
            'username': username,
            'password': password,
            'secret': device.split(':')[4],
            'device_type': 'cisco_ios'
        })
    # device_json = json.dumps(devices, indent=4)
    # print(device_json)

commands = ['terminal length 0', 'show ip int brief', 'show run']

def run(dev, cmds):
    with netmiko.ConnectHandler(**dev) as ssh:
        prompt = ssh.find_prompt()
        hostname = prompt.rstrip('#')
        # print(hostname)
        for cmd in cmds:
            output = ssh.send_command(cmd)
            filename = f'{hostname}-{cmd[:10]}' + '.txt'
            with open(filename, 'w') as f:
                f.write(prompt.rstrip('#') + '\n')
                f.write(output)


th_list = []

for device in devices:
    th = threading.Thread(target=run, args=(device,commands))
    th_list.append(th)

for i,th in enumerate(th_list):
    th.start()
    print(f'started thread {i}')

for th in th_list:
    th.join()

##
## Configure ACL
##

device = {
    'host': '10.1.1.10',
    'port': '22',
    'username': 'u1',
    'password': 'cisco',
    'secret': 'cisco',
    'device_type': 'cisco_ios'
}

ssh = netmiko.ConnectHandler(**device)
ssh.config_mode()
# single method calls:
# print('Sending command: access-list 101 permit tcp any any eq 80')
# ssh.send_command('access-list 101 permit tcp any any eq 80')
# print('Sending command: access-list 101 permit tcp any any eq 443')
# ssh.send_command('access-list 101 permit tcp any any eq 443')
# print('Sending command: access-list 101 deny ip any any')
# ssh.send_command('access-list 101 deny ip any any')

# commands set method:
# commands = ['no access-list 101 permit tcp any any eq 80',
#             'no access-list 101 permit tcp any any eq 443',
#             'no access-list 101 deny ip any any']
#
# ssh.send_config_set(commands)

ssh.exit_config_mode()
config = ssh.send_command('show run')
print(config)

##
## Configure RIP with commands from file
##
device = {
    'host': '10.1.1.10',
    'port': '22',
    'username': 'u1',
    'password': 'cisco',
    'secret': 'cisco',
    'device_type': 'cisco_ios'
}


with netmiko.ConnectHandler(**device) as ssh:
    ssh.send_config_from_file('rip_config.txt', enter_config_mode=True, exit_config_mode=True)  # enters config mode before sending commans and exits after commands
    print(ssh.send_command('show run'))


##
## Configure RIP with commands from file
##
device = {
    'host': '',
    'port': '22',
    'username': 'u1',
    'password': 'cisco',
    'secret': 'cisco',
    'device_type': 'cisco_ios'
}

device_ips = ['10.1.1.10', '10.1.1.20', '10.1.1.30']

for ip in device_ips:
    device['host'] = ip
    print(device)
    with netmiko.ConnectHandler(**device) as ssh:
        output = ssh.send_command('show ip interface brief')
        print(output)

##
## Configure RIP with commands from file and write output to file
##
from datetime import datetime

device = {
    'host': '',
    'port': '22',
    'username': 'u1',
    'password': 'cisco',
    'secret': 'cisco',
    'device_type': 'cisco_ios'
}

device_ips = ['10.1.1.10', '10.1.1.20', '10.1.1.30']

for ip in device_ips:
    device['host'] = ip
    print(device)
    with netmiko.ConnectHandler(**device) as ssh:
        output = ssh.send_command('show ip interface brief')
        prompt = ssh.find_prompt().rsplit('#')
        year = datetime.now().year
        month = datetime.now().month
        day = datetime.now().day
        filename = f'f{prompt}-{day}-{month}-{year}'
        with open(filename, 'w') as f:
            f.write(output)

##
## the function called execute() that has 2 arguments: a device of type dictionary and a command to execute on that device
##
device = {
    'host': '10.1.1.10',
    'port': '22',
    'username': 'u1',
    'password': 'cisco',
    'secret': 'cisco',
    'device_type': 'cisco_ios'
}

def execute(dev, cmd):
    with netmiko.ConnectHandler(**dev) as ssh:
        output = ssh.send_command(cmd)
        return output

execute(device, 'show run')

##
## the function called execute() that has 2 arguments: a device of type dictionary and a command list to execute on that device
##
device = {
    'host': '10.1.1.10',
    'port': '22',
    'username': 'u1',
    'password': 'cisco',
    'secret': 'cisco',
    'device_type': 'cisco_ios'
}

cmd = ['no router rip', 'int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'end', 'sh ip int loopback 0']

def execute(dev, cmd):
    with netmiko.ConnectHandler(**dev) as ssh:
        output = ssh.send_config_set(cmd, enter_config_mode=True, exit_config_mode=True)
        return output

execute(device, cmd)

##
## the function called execute() will be called on multiple devices with separate commands
##
devices = [{
    'host': '10.1.1.10',
    'port': '22',
    'username': 'u1',
    'password': 'cisco',
    'secret': 'cisco',
    'device_type': 'cisco_ios'
},
{
    'host': '10.1.1.20',
    'port': '22',
    'username': 'u1',
    'password': 'cisco',
    'secret': 'cisco',
    'device_type': 'cisco_ios'
},
{
    'host': '10.1.1.30',
    'port': '22',
    'username': 'u1',
    'password': 'cisco',
    'secret': 'cisco',
    'device_type': 'cisco_ios'
},
]

def execute(dev, cmd):
    with netmiko.ConnectHandler(**dev) as ssh:
        output = ssh.send_command(cmd)
        return output

for device in devices:
    cmd = input(f'Enter command for {device["host"]}: ')
    try:
        execute(device, cmd)
    except Exception as e:
        print(e)

##
## the function called execute() will be called on multiple devices concurently
##
import threading
devices = [{
    'host': '10.1.1.10',
    'port': '22',
    'username': 'u1',
    'password': 'cisco',
    'secret': 'cisco',
    'device_type': 'cisco_ios'
},
{
    'host': '10.1.1.20',
    'port': '22',
    'username': 'u1',
    'password': 'cisco',
    'secret': 'cisco',
    'device_type': 'cisco_ios'
},
{
    'host': '10.1.1.30',
    'port': '22',
    'username': 'u1',
    'password': 'cisco',
    'secret': 'cisco',
    'device_type': 'cisco_ios'
},
]

cmds_list = [['show run', 'show ip int brief'], ['show run', 'show ip int brief'], ['show run', 'show ip int brief']]

routers = zip(devices, cmds_list)


def execute(dev, cmd_list):
    try:
        with netmiko.ConnectHandler(**dev) as ssh:
            output = ssh.send_config_set(cmd_list)
            return output
    except Exception as e:
        print(e)


th_list = []

for router, cmd_lst in routers:
    thread = threading.Thread(target=execute, args=(router, cmd_lst,))
    th_list.append(thread)

for thread in th_list:
    thread.start()

for thread in th_list:
    thread.join()


###
### compare execution time for sequential vs concurential
###
from datetime import datetime

start = datetime.utcnow()
devices = [{
    'host': '10.1.1.10',
    'port': '22',
    'username': 'u1',
    'password': 'cisco',
    'secret': 'cisco',
    'device_type': 'cisco_ios'
},
{
    'host': '10.1.1.20',
    'port': '22',
    'username': 'u1',
    'password': 'cisco',
    'secret': 'cisco',
    'device_type': 'cisco_ios'
},
{
    'host': '10.1.1.30',
    'port': '22',
    'username': 'u1',
    'password': 'cisco',
    'secret': 'cisco',
    'device_type': 'cisco_ios'
},
]

def execute(dev, cmd_list):
    with netmiko.ConnectHandler(**dev) as ssh:
        output = ssh.send_config_set(cmd_list)
        return output

cmds_list = [['show run', 'show ip int brief'], ['show run', 'show ip int brief'], ['show run', 'show ip int brief']]

for device in devices:
    try:
        execute(device, cmds_list)
    except Exception as e:
        print(e)

end = datetime.utcnow()
total_seq = end-start


import threading
from datetime import datetime

start = datetime.utcnow()
devices = [{
    'host': '10.1.1.10',
    'port': '22',
    'username': 'u1',
    'password': 'cisco',
    'secret': 'cisco',
    'device_type': 'cisco_ios'
},
{
    'host': '10.1.1.20',
    'port': '22',
    'username': 'u1',
    'password': 'cisco',
    'secret': 'cisco',
    'device_type': 'cisco_ios'
},
{
    'host': '10.1.1.30',
    'port': '22',
    'username': 'u1',
    'password': 'cisco',
    'secret': 'cisco',
    'device_type': 'cisco_ios'
},
]

cmds_list = [['show run', 'show ip int brief'], ['show run', 'show ip int brief'], ['show run', 'show ip int brief']]

routers = zip(devices, cmds_list)


def execute(dev, cmd_list):
    try:
        with netmiko.ConnectHandler(**dev) as ssh:
            output = ssh.send_config_set(cmd_list)
            return output
    except Exception as e:
        print(e)


th_list = []

for router, cmd_lst in routers:
    thread = threading.Thread(target=execute, args=(router, cmd_lst,))
    th_list.append(thread)

for thread in th_list:
    thread.start()

for thread in th_list:
    thread.join()
end = datetime.utcnow()
total_conc = end-start

print(f'{total_seq.total_seconds()} - sequential time')
print(f'{total_conc.total_seconds()} - concurential time')
