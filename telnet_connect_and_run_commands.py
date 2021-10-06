import telnetlib
import time

host = '10.1.1.20'
port = '23'
user = 'u1'
password = 'cisco'

tn = telnetlib.Telnet(host=host, port=port)

tn.read_until(b'Username: ')
tn.write(user.encode() + b'\n')
tn.write(password.encode() + b'\n')

tn.write(b'terminal length 0\n')
tn.write(b'show ip int brief\n')
tn.write(b'exit\n')

time.sleep(1)

output = tn.read_all()
print(type(output))
print(output.decode())