import my_paramiko_connect
import datetime
import threading

def backup(router):
    ssh_client = my_paramiko_connect.connect(**router)
    shell = my_paramiko_connect.get_shell(ssh_client)

    my_paramiko_connect.send_command(shell, 'terminal length 0')
    my_paramiko_connect.send_command(shell, 'enable')
    my_paramiko_connect.send_command(shell, 'cisco')
    my_paramiko_connect.send_command(shell, 'show running-config')

    output = my_paramiko_connect.show(shell)
    output_list = output.splitlines()

    def extract_run_config(begin_str, end_str):
        i1, i2 = 0, 0
        for idx in range(len(output_list)):
            if begin_str in output_list[idx] and not i1:  # only first occurence of the begin_str
                i1 = idx
            if end_str in output_list[idx]:
                i2 = idx + 1
        run_config = '\n'.join(output_list[i1:i2]) + '\n'
        return run_config

    run_config = extract_run_config('version', 'end')

    year = datetime.date.today().year
    month = datetime.date.today().month
    day = datetime.date.today().day
    filename = '{}-{}-{}-{}.txt'.format(router['hostname'], year, month, day)

    with open(filename, 'w') as f:
        f.write(run_config)

    my_paramiko_connect.close(ssh_client)

router1 = {'hostname': '10.1.1.10', 'port': '22', 'username': 'u1', 'password': 'cisco'}
router2 = {'hostname': '10.1.1.20', 'port': '22', 'username': 'u1', 'password': 'cisco'}
router3 = {'hostname': '10.1.1.30', 'port': '22', 'username': 'u1', 'password': 'cisco'}
routers = [router1, router2, router3]

#list storing the threads
threads = list()

for router in routers:
    th = threading.Thread(target=backup, args=(router,))
    threads.append(th)

#starting threads
for th in threads:
    th.start()

#waiting for threads to finish
for th in threads:
    th.join()
