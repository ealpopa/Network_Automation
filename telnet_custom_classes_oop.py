class TelnetDevice:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.tn = None
        self.output = ''

    def connect(self):
        import telnetlib
        try:
            print(f"Connecting to {self.host}...")
            self.tn = telnetlib.Telnet(self.host, self.port)
        except Exception as e:
            print(e)

    def authenticate(self):
        self.tn.read_until(b'Username: ')
        self.tn.write(self.username.encode() + b'\n')
        self.tn.read_until(b'Password: ')
        self.tn.write(self.password.encode() + b'\n')
        print("Successfully connected")
        self.tn.write('terminal length 0\n'.encode())

    def disconnect(self):
        import time
        self.tn.write(b'exit\n')
        time.sleep(1)

    def send_command(self, command):
        # self.__connect()
        # self.__authenticate()
        self.tn.write(f'{command}\n'.encode())
        print(f"Just sent command: {command}")

    def show_output(self):
        self.output = self.tn.read_all()
        print(self.output.decode())


if __name__ == '__main__':

    ips = ['10.1.1.10', '10.1.1.20', '10.1.1.30']

    device = {
        'host': '10.1.1.20',
        'port': '23',
        'username': 'u1',
        'password': 'cisco'
    }

    for ip in ips:
        # device['host'] = ip
        connection = TelnetDevice(**device)
        connection.connect()
        connection.authenticate()
        connection.send_command('show ip interface brief')
        connection.send_command('show interfaces')
        connection.disconnect()
        connection.show_output()


###
### Higher abstraction implementation:
###


class TelnetDevice:

    def __init__(self, host, username, password, port='23', config=None):  ## config usef in case dictionary with config file is passed in kwargs
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.tn = None
        self.output = ''

        self.__connect()
        self.__authenticate()

    def __connect(self):
        import telnetlib
        try:
            print(f"Connecting to {self.host}...")
            self.tn = telnetlib.Telnet(self.host, self.port)
        except Exception as e:
            print(e)

    def __authenticate(self):
        self.tn.read_until(b'Username: ')
        self.tn.write(self.username.encode() + b'\n')
        self.tn.read_until(b'Password: ')
        self.tn.write(self.password.encode() + b'\n')
        print("Successfully connected")
        self.tn.write('terminal length 0\n'.encode())

    def __disconnect(self):
        import time
        self.tn.write(b'exit\n')
        time.sleep(1)

    def send_command(self, command):
        self.tn.write(f'{command}\n'.encode())
        print(f"Just sent command: {command}")

    def send_commands_list(self, commands_list):
        for command in commands_list:
            self.send_command(command)

    def send_commands_from_file(self, file):
        with open(file) as f:
            commands_list = f.read().splitlines()
            self.send_commands_list(commands_list)

    def get_output(self):
        self.__disconnect()
        self.output = self.tn.read_all()
        return self.output

    def print_output(self):
        print(self.get_output().decode())

    def save_output(self, file):
        with open(file, 'w') as f:
            f.write(self.get_output().decode())


if __name__ == '__main__':
    # from getpass import getpass
    ips = ['10.1.1.10', '10.1.1.20', '10.1.1.30']

    device_template = {
        'host': '10.1.1.20',
        'port': '23',
        'username': 'u1',
        'password': 'cisco'
    }

    for ip in ips:
        # password = getpass(f"Please insert password for host {ip}: ")
        # device_template['password'] = password
        device_template['host'] = ip

        connection = TelnetDevice(**device_template)
        # connection.send_command('show ip interface brief')
        # connection.send_command('show interfaces')
        connection.send_commands_from_file('commands.txt')
        # connection.print_output()
        filename = f"{ip}-command-output.txt"
        connection.save_output(filename)

###
### Use dictionary containing config files as kwarg
###
    r1 = {'host': '10.1.1.10', 'username': 'u1', 'password': 'cisco', 'config': 'ospf.txt'}
    r2 = {'host': '10.1.1.20', 'username': 'u1', 'password': 'cisco', 'config': 'eigrp.txt'}
    r3 = {'host': '10.1.1.30', 'username': 'u1', 'password': 'cisco', 'config': 'router3.conf'}

    for device in [r1, r2, r3]:
        connection = TelnetDevice(**device)
        connection.send_commands_from_file(device['config'])
        # filename = f"{device['host']}-command-output.txt"
        # connection.save_output(filename)
