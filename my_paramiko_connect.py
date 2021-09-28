import paramiko
import time

def connect(hostname, port, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print('Connecting to {}'.format(hostname))
    ssh_client.connect(hostname=hostname, port=port, username=username, password=password, look_for_keys=False, allow_agent=False)
    return ssh_client

def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell

def send_command(shell, cmd, timeout=1):
    print('Sending command: {}'.format(cmd))
    shell.send(cmd + '\n')
    time.sleep(timeout)

def show(shell, n=10000):
    output = shell.recv(n)
    return output.decode()

def close(ssh_client):
    if ssh_client.get_transport().is_active():
        print('Closing connection.')
        ssh_client.close()

if __name__ == '__main__':

    router1 = {'hostname': '10.1.1.10', 'port': '22', 'username': 'u1', 'password': 'cisco'}

    ssh_client = connect(**router1)
    shell = get_shell(ssh_client)
    send_command(shell, 'enable')
    send_command(shell, 'cisco')
    send_command(shell, 'terminal length 0')
    send_command(shell, 'sh version')
    send_command(shell, 'sh ip int br')

    output = show(shell)
    print(output)
    close(ssh_client)
