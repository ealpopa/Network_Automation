import paramiko
import time
import getpass

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

router1 = {'hostname': '10.1.1.10', 'port': '22', 'username': 'u1', 'password': 'cisco'}
router2 = {'hostname': '10.1.1.20', 'port': '22', 'username': 'u1', 'password': 'cisco'}
router3 = {'hostname': '10.1.1.30', 'port': '22', 'username': 'u1', 'password': 'cisco'}

routers = [router1, router2, router3]

for router in routers:
    print('Connecting to {}'.format(router['hostname']))
    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
    shell = ssh_client.invoke_shell()

    shell.send('enable\n')
    shell.send('cisco\n')
    shell.send('configure terminal\n')
    shell.send('router ospf 1\n')
    shell.send('network 0.0.0.0 0.0.0.0 area 0\n')
    shell.send('end\n')
    shell.send('terminal length 0\n')
    shell.send('sh ip protocols\n')

    time.sleep(2)
    output = shell.recv(10000)
    output = output.decode('utf-8')
    print(output)

if ssh_client.get_transport().is_active():
    print('Closing connection.')
    ssh_client.close()