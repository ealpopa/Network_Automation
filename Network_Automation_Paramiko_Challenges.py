# #Challenge 1 - Connect to router and show users
#
#
# import paramiko
# import time
#
# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#
# router = {'hostname': '10.1.1.10', 'port': '22', 'username': 'u1', 'password': 'cisco'}
#
# print('Connecting to {}'.format(router['hostname']))
#
# ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
# shell = ssh_client.invoke_shell()
#
# shell.send('show users\n')
# time.sleep(1)
# output = shell.recv(10000).decode()
# print(output)
#
# if ssh_client.get_transport().is_active():
#     print('Closing connection...')
#     ssh_client.close()
#
#
# #Challenge 2 - Get SSH password securely
#
#
# import paramiko
# import time
# import getpass
#
# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#
# password = getpass.getpass('Enter SSH password: ')
# router = {'hostname': '10.1.1.10', 'port': '22', 'username': 'u1', 'password': password}
#
# print('Connecting to {}'.format(router['hostname']))
#
# ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
# shell = ssh_client.invoke_shell()
#
# shell.send('show users\n')
# time.sleep(1)
# output = shell.recv(10000).decode()
# print(output)
#
# if ssh_client.get_transport().is_active():
#     print('Closing connection...')
#     ssh_client.close()

# #Challenge 3 - Save output to file instead of printing it
#
#
# import paramiko
# import time
#
# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#
# router = {'hostname': '10.1.1.10', 'port': '22', 'username': 'u1', 'password': 'cisco'}
#
# print('Connecting to {}'.format(router['hostname']))
#
# ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
# shell = ssh_client.invoke_shell()
#
# shell.send('show users\n')
# time.sleep(1)
# output = shell.recv(10000).decode()
#
# with open('command_output.txt', 'w') as f:
#     f.write(output)
#
# if ssh_client.get_transport().is_active():
#     print('Closing connection...')
#     ssh_client.close()


# #Challenge 4 - Connect to router, enter enable mode, show running-config, save output to file
#
#
# import paramiko
# import time
#
# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#
# router = {'hostname': '10.1.1.10', 'port': '22', 'username': 'u1', 'password': 'cisco'}
#
# print('Connecting to {}'.format(router['hostname']))
#
# ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
# shell = ssh_client.invoke_shell()
#
# shell.send('enable\n')
# shell.send('terminal length 0\n')
# shell.send('show running-config\n')
# time.sleep(1)
# output = shell.recv(10000).decode()
#
# filename = '{}'.format(router['hostname']) + '-running-config' + '.txt'
#
# with open(filename, 'w') as f:
#     f.write(output)
#
# if ssh_client.get_transport().is_active():
#     print('Closing connection...')
#     ssh_client.close()


# #Challenge 5 - Connect to router and execute commands stored in a list
#
#
# import paramiko
# import time
#
# commands = ['enable', 'cisco', 'conf t', 'username admin1 secret cisco', 'access-list 1 permit any', 'end', 'terminal length 0', 'sh run | i user']
#
# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#
# router = {'hostname': '10.1.1.10', 'port': '22', 'username': 'u1', 'password': 'cisco'}
#
# print('Connecting to {}'.format(router['hostname']))
#
# ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
# shell = ssh_client.invoke_shell()
#
# for cmd in commands:
#     shell.send(cmd + '\n')
#     time.sleep(1)
#
# output = shell.recv(10000).decode()
# print(output)
#
# if ssh_client.get_transport().is_active():
#     print('Closing connection...')
#     ssh_client.close()


# #Challenge 6 - Connect to router and execute commands stored in a text file
#
#
# import paramiko
# import time
#
# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#
# router = {'hostname': '10.1.1.10', 'port': '22', 'username': 'u1', 'password': 'cisco'}
#
# print('Connecting to {}'.format(router['hostname']))
#
# ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
# shell = ssh_client.invoke_shell()
#
# with open('commands.txt') as f:
#     command_lines = f.readlines()
#     for cmd in command_lines:
#         shell.send(cmd)
#
# time.sleep(1)
# output = shell.recv(10000).decode()
# print(output)
#
# if ssh_client.get_transport().is_active():
#     print('Closing connection...')
#     ssh_client.close()


# #Challenge 7 - Simplify paramiko connection to take commands from a list as an argument
#
#
# import paramiko
# import time
#
# def connect(hostname, port, username, password):
#     ssh_client = paramiko.SSHClient()
#     ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     print('Connecting to {}'.format(hostname))
#     ssh_client.connect(hostname=hostname, port=port, username=username, password=password, look_for_keys=False, allow_agent=False)
#     return ssh_client
#
# def get_shell(ssh_client):
#     shell = ssh_client.invoke_shell()
#     return shell
#
# def send_from_list(shell, cmd_lst, timeout=1):
#     for cmd in cmd_lst:
#         print('Sending command: {}'.format(cmd))
#         shell.send(cmd + '\n')
#         time.sleep(timeout)
#
# def show(shell, n=10000):
#     output = shell.recv(n)
#     return output.decode()
#
# def close(ssh_client):
#     if ssh_client.get_transport().is_active():
#         print('Closing connection.')
#         ssh_client.close()
#
# if __name__ == '__main__':
#
#     router1 = {'hostname': '10.1.1.10', 'port': '22', 'username': 'u1', 'password': 'cisco'}
#     cmd_lst = ['enable', 'terminal length 0', 'sh version', 'sh ip int br']
#
#     ssh_client = connect(**router1)
#     shell = get_shell(ssh_client)
#     send_from_list(shell, cmd_lst)
#
#     output = show(shell)
#     print(output)
#     close(ssh_client)


# # Challenge 8 - Simplify paramiko connection to take commands from a file as an argument
#
#
# import paramiko
# import time
#
# def connect(hostname, port, username, password):
#     ssh_client = paramiko.SSHClient()
#     ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     print('Connecting to {}'.format(hostname))
#     ssh_client.connect(hostname=hostname, port=port, username=username, password=password, look_for_keys=False, allow_agent=False)
#     return ssh_client
#
# def get_shell(ssh_client):
#     shell = ssh_client.invoke_shell()
#     return shell
#
# def send_from_file(shell, filename, timeout=1):
#     with open(filename) as f:
#         cmd_lst = f.readlines()
#         for cmd in cmd_lst:
#             print('Sending command: {}'.format(cmd))
#             shell.send(cmd)
#             time.sleep(timeout)
#
# def show(shell, n=10000):
#     output = shell.recv(n)
#     return output.decode()
#
# def close(ssh_client):
#     if ssh_client.get_transport().is_active():
#         print('Closing connection.')
#         ssh_client.close()
#
# if __name__ == '__main__':
#
#     router1 = {'hostname': '10.1.1.10', 'port': '22', 'username': 'u1', 'password': 'cisco'}
#
#     ssh_client = connect(**router1)
#     shell = get_shell(ssh_client)
#     send_from_file(shell, 'commands.txt')
#
#     output = show(shell)
#     print(output)
#     close(ssh_client)


# Challenge 9 - Multi-router topology with details stored in a dictionary. commands are in a file referenced by the dict


# import paramiko
# import time
#
# def connect(hostname, port, username, password, config):
#     ssh_client = paramiko.SSHClient()
#     ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     print('Connecting to {}'.format(hostname))
#     ssh_client.connect(hostname=hostname, port=port, username=username, password=password, look_for_keys=False, allow_agent=False)
#     return ssh_client
#
# def get_shell(ssh_client):
#     shell = ssh_client.invoke_shell()
#     return shell
#
# def send_from_file(shell, filename, timeout=1):
#     with open(filename) as f:
#         cmd_lst = f.readlines()
#         for cmd in cmd_lst:
#             print('Sending command: {}'.format(cmd))
#             shell.send(cmd)
#             time.sleep(timeout)
#
# def show(shell, n=10000):
#     output = shell.recv(n)
#     return output.decode()
#
# def close(ssh_client):
#     if ssh_client.get_transport().is_active():
#         print('Closing connection.')
#         ssh_client.close()
#
# if __name__ == '__main__':
#
#     router1 = {'hostname': '10.1.1.10', 'port': '22', 'username': 'u1', 'password': 'cisco',
#                'config': 'ospf.txt'}
#
#     router2 = {'hostname': '10.1.1.20', 'port': '22', 'username': 'u1', 'password': 'cisco',
#                'config': 'eigrp.txt'}
#
#     router3 = {'hostname': '10.1.1.30', 'port': '22', 'username': 'u1', 'password': 'cisco',
#                'config': 'router3.conf'}
#
#     routers = [router1, router2, router3]
#
#     for router in routers:
#         ssh_client = connect(**router)
#         shell = get_shell(ssh_client)
#         send_from_file(shell, router['config'])
#         output = show(shell)
#         print(output)
#         close(ssh_client)


# Challenge 10 - Previous challenge with multithreading


import paramiko
import time
import threading

def connect(hostname, port, username, password, config):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print('Connecting to {}'.format(hostname))
    ssh_client.connect(hostname=hostname, port=port, username=username, password=password, look_for_keys=False, allow_agent=False)
    return ssh_client

def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell

def send_from_file(shell, filename, timeout=1):
    with open(filename) as f:
        cmd_lst = f.readlines()
        for cmd in cmd_lst:
            print('Sending command: {}'.format(cmd))
            shell.send(cmd)
            time.sleep(timeout)

def show(shell, n=10000):
    output = shell.recv(n)
    return output.decode()

def close(ssh_client):
    if ssh_client.get_transport().is_active():
        print('Closing connection.')
        ssh_client.close()

if __name__ == '__main__':

    def run(router):
        ssh_client = connect(**router)
        shell = get_shell(ssh_client)
        send_from_file(shell, router['config'])
        output = show(shell)
        print(output)
        close(ssh_client)

    router1 = {'hostname': '10.1.1.10', 'port': '22', 'username': 'u1', 'password': 'cisco',
               'config': 'ospf.txt'}

    router2 = {'hostname': '10.1.1.20', 'port': '22', 'username': 'u1', 'password': 'cisco',
               'config': 'eigrp.txt'}

    router3 = {'hostname': '10.1.1.30', 'port': '22', 'username': 'u1', 'password': 'cisco',
               'config': 'router3.conf'}

    routers = [router1, router2, router3]

    threads = []

    for router in routers:
        th = threading.Thread(target=run, args=(router,))
        threads.append(th)

    for th in threads:
        th.start()

    for th in threads:
        th.join()
