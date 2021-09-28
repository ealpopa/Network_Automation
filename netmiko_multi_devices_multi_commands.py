from netmiko import ConnectHandler

with open('devices.txt') as f:
    devices = f.read().splitlines()

device_list = list()

for ip in devices:
    cisco_device = {
        'host': ip,
        'port': '22',
        'username': 'u1',
        'password': 'cisco',
        'device_type': 'cisco_ios',
        'secret': 'cisco',
        'verbose': True
    }
    device_list.append(cisco_device)

for device in device_list:
    connection = ConnectHandler(**device)

    print('Entering the enable mode...')
    connection.enable()

    filename = input('Please enter config filename with path for device {}: '.format(device['host']))

    print('Sending commands from file {}'.format(filename))
    output = connection.send_config_from_file(filename)
    print(output)

    print('Closing connection with {}'.format(device['host']))
    connection.disconnect()

    print('*' * 30)


####
#Store filenames in list
####
# from netmiko import ConnectHandler
#
# with open('devices.txt') as f:
#     devices = f.read().splitlines()
#
# device_list = list()
#
# for ip in devices:
#     cisco_device = {
#         'host': ip,
#         'port': '22',
#         'username': 'u1',
#         'password': 'cisco',
#         'device_type': 'cisco_ios',
#         'secret': 'cisco',
#         'verbose': True
#     }
#     device_list.append(cisco_device)
#
# filenames = ['CiscoRouter1.txt', 'CiscoRouter2.txt', 'CiscoRouter3.txt']
#
# for idx in range(len(device_list)):
#     connection = ConnectHandler(**device_list[idx])
#
#     print('Entering the enable mode...')
#     connection.enable()
#
#     # filename = input('Please enter config filename with path for device {}: '.format(device['host']))
#
#     print('Sending commands from file {}'.format(filenames[idx]))
#     output = connection.send_config_from_file(filenames[idx])
#     print(output)
#
#     print('Closing connection with {}'.format(device_list[idx]['host']))
#     connection.disconnect()
#
#     print('*' * 30)