import telnetlib
import time

ips = ['10.1.1.10', '10.1.1.20', '10.1.1.30']

device = {
    'host': '',
    'port': '23',
    'username': 'u1',
    'password': 'cisco'
}

for ip in ips:
    device['host'] = ip
    print(f"Connecting to {device['host']}...")
    try:
        tn = telnetlib.Telnet(device['host'], device['port'])

        tn.read_until(b'Username: ')
        tn.write(device['username'].encode() + b'\n')
        tn.read_until(b'Password: ')
        tn.write(device['password'].encode() + b'\n')

        tn.write(b'terminal length 0\n')
        tn.write(b'show ip int brief\n')
        tn.write(b'exit\n')

        time.sleep(1)

        output = tn.read_all()
        print(type(output))
        print(output.decode())
    except Exception as e:
        print(e)
