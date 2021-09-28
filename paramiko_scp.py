import paramiko
from scp import SCPClient
import os

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ubuntu = {'hostname': '192.168.0.220', 'port': '22', 'username': 'osboxes', 'password': 'osboxes.org'}
ssh_client.connect(**ubuntu, look_for_keys=False, allow_agent=False)
scp = SCPClient(ssh_client.get_transport())

#copy a single file
scp.put(os.path.abspath(os.getcwd()) + '\\Output files\\devices.txt', '/tmp/aa.txt')

#copy a directory
scp.put('Output files', recursive=True, remote_path='/tmp')

scp.get('/etc/passwd', 'C:\\Users\\popam')
scp.close()
