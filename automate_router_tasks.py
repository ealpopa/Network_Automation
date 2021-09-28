import my_paramiko_connect

ssh_client = my_paramiko_connect.connect('10.1.1.30', '22', 'u1', 'cisco')
shell = my_paramiko_connect.get_shell(ssh_client)
my_paramiko_connect.send_command(shell, 'show version')
my_paramiko_connect.send_command(shell, 'terminal length 0')
my_paramiko_connect.send_command(shell, 'show ip interface brief')
# my_paramiko_connect.show(shell) #flush the buffer and show only the output for the last command
my_paramiko_connect.send_command(shell, 'show ip protocols')
output = my_paramiko_connect.show(shell)
print(output)
my_paramiko_connect.close(ssh_client)