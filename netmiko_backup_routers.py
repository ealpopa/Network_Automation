from netmiko import ConnectHandler
from datetime import datetime
from threading import Thread

devices_list = list()

def backup(ip_list):
    for ip in ip_list:
        Cisco_device = {
        'host': ip,
        'port': '22',
        'username': 'u1',
        'password': 'cisco',
        'device_type': 'cisco_ios',
        'secret': 'cisco',
        'verbose': True
        }

        connection = ConnectHandler(**Cisco_device)
        print('Entering the enable mode')
        connection.enable()

        prompt = connection.find_prompt()
        year = datetime.now().year
        month = datetime.now().month
        day = datetime.now().day
        filename = f'{prompt[:-1]}-{day}{month}{year}-backup.txt'

        output = connection.send_command('show run')
        with open(filename, 'w') as backup_file:
            backup_file.write(output)
        print(f'Wrote backup for {prompt[:-1]} successfully')
        print('Closing connection')
        connection.disconnect()
        print('*' * 20)


with open('devices.txt') as f:
    ips_list = f.read().splitlines()

    th_list = []
    for ip in ips_list:
        thread = Thread(target=backup, args=(ips_list,))
        th_list.append(thread)

    for thread in th_list:
        thread.start()

    for thread in th_list:
        thread.join()
