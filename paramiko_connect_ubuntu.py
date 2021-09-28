import my_paramiko_connect
import getpass

username = input('Username: ')
password = getpass.getpass('Enter password: ')

ubuntu = {'hostname': '192.168.0.220', 'port': '22', 'username': username, 'password': password}

ssh_client = my_paramiko_connect.connect(**ubuntu)
shell = my_paramiko_connect.get_shell(ssh_client)

new_user = input('Username to be created: ')
my_paramiko_connect.send_command(shell, 'sudo useradd -m -d /home/user2 -s /bin/bash ' + new_user)
my_paramiko_connect.send_command(shell, password)

option = input('Do you want to display all the users? [y/n]')

if option == 'y':
    my_paramiko_connect.send_command(shell, 'cat /etc/passwd')
    users = my_paramiko_connect.show(shell)
    print(users)

my_paramiko_connect.close(shell)
