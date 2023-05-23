import os
import time

with open('Segurança da informação\pingmultipllo\hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()
    
    for ip in dump:
        print("-" * 50)
        print("Verificando o ip: ", ip)
        os.system('ping -n 2 {}'.format(ip))
        time.sleep(3)