from netmiko import ConnectHandler

cisco_device = {
    'host': '10.1.1.10',
    'port': '22',
    'username': 'u1',
    'password': 'cisco',
    'device_type': 'cisco_ios',
    'secret': 'cisco',
    'verbose': True
}

connection = ConnectHandler(**cisco_device)
print('Entering the enable mode...')
connection.enable()

# commands = ['int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'exit', 'username netmiko secret cisco']
# output = connection.send_config_set(commands)

# commands = 'int loopback 0;ip address 1.1.1.1 255.255.255.255;exit;username netmiko secret cisco'
# output = connection.send_config_set(commands.split(';'))

# commands = '''ip ssh version 2
# access-list 1 permit any
# ip domain-name net-auto.io
# '''
# output = connection.send_config_set(commands.split('\n'))

print('Sending commands from file...')
output = connection.send_config_from_file('ospf.txt')
print(output)
print(connection.find_prompt())
connection.send_command('write memory')

print('Closing connection...')
connection.disconnect()
